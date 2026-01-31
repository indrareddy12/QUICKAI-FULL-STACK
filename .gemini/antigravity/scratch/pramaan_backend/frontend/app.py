import streamlit as st
import io
from pypdf import PdfReader
from legal_docu import analyze_legal_text

# Page Configuration
st.set_page_config(
    page_title="Pramaan AI - Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.title("⚖️ Pramaan AI Legal Assistant")
st.markdown("### Advanced Legal Analysis & Dossier Generation")
st.divider()

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2237/2237583.png", width=100) # Placeholder icon
    st.markdown("### About Pramaan")
    st.info(
        "Pramaan AI uses advanced Multi-Agent systems to analyze legal documents, "
        "identify relevant IPC/CrPC sections, and suggest actionable legal strategies."
    )
    st.markdown("---")
    st.write("v2.0 (Production Level)")

# Input Section
col1, col2 = st.columns([1, 1])

legal_text = ""

with col1:
    st.subheader("📤 Document Upload")
    uploaded_file = st.file_uploader(
        "Upload PDF or Text file", 
        type=["pdf", "txt"],
        help="Upload FIRs, Petitions, or Agreements"
    )
    
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                pdf_reader = PdfReader(uploaded_file)
                legal_text = "".join([p.extract_text() for p in pdf_reader.pages])
                st.success(f"✅ Extracted {len(legal_text)} characters from PDF")
            else:
                legal_text = uploaded_file.read().decode("utf-8")
                st.success("✅ Text file loaded")
        except Exception as e:
            st.error(f"Error reading file: {e}")

with col2:
    st.subheader("📝 Direct Input")
    text_input = st.text_area(
        "Paste legal case details here...", 
        height=200,
        placeholder="Type the case description or paste text..."
    )
    if text_input:
        legal_text = text_input

# Analysis Trigger
if st.button("Generate Comprehensive Legal Dossier", type="primary"):
    if not legal_text.strip():
        st.warning("Please upload a document or enter text to proceed.")
    else:
        with st.spinner("🤖 Orchestrating Agents: Intake -> Research -> Analysis..."):
            try:
                # Call the Production Backend Service
                result = analyze_legal_text(legal_text)
                
                if "error" in result:
                     st.error(f"Analysis Failed: {result['error']}")
                else:
                    # Display Results using Tabs for clean UI
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "📋 Applicable Laws", 
                        "📊 Case Strength", 
                        "📝 Recommended Actions", 
                        "🔍 Evidence Needed"
                    ])
                    
                    with tab1:
                        st.subheader("Relevant Legal Sections")
                        sections = result.get("applicable_sections", [])
                        if not sections:
                            st.info("No specific sections identified.")
                        for section in sections:
                            with st.expander(f"{section.get('code')} {section.get('section')} - {section.get('title')}", expanded=True):
                                st.write(f"**Description:** {section.get('description')}")
                                st.write(f"**Punishment:** {section.get('punishment')}")
                                st.caption(f"Relevance: {section.get('relevance')}")
                    
                    with tab2:
                        st.subheader("Case Strength Analysis")
                        strength = result.get("case_strength", {})
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("Win Probability Score", f"{strength.get('score', 0)}/100")
                            st.write(f"**Likelihood:** {strength.get('likelihood', 'Unknown').upper()}")
                        
                        with col_b:
                            st.write("**Key Strengths:**")
                            for s in strength.get("strengths", []):
                                st.success(f"✅ {s}")
                            
                            st.write("**Weaknesses:**")
                            for w in strength.get("weaknesses", []):
                                st.error(f"⚠️ {w}")

                    with tab3:
                        st.subheader("Strategic Recommendations")
                        actions = result.get("recommended_actions", [])
                        for i, action in enumerate(actions, 1):
                            st.info(f"{i}. {action}")
                            
                    with tab4:
                        st.subheader("Evidence Requirements")
                        evidence = result.get("evidence_requirements", [])
                        for item in evidence:
                            priority_color = "red" if item.get("priority") == "critical" else "orange"
                            st.markdown(f":{priority_color}[**{item.get('priority').upper()}**] : **{item.get('type')}**")
                            st.write(f"{item.get('description')}")
                            st.divider()
                            
            except Exception as e:
                st.error(f"System Error: {str(e)}")
