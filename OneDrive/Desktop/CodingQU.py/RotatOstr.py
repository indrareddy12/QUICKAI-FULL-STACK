#rotating of a string of one step means each word of that string shfited by one positon 
#left and the lleftmost word will go the rightmost position.you are given a string str 
#and an integer k. you are required to rotate the string str as mentioned above.by  k 
#steps and print the  rotated string str.

def main():
    l=int(input())
    st=input()
    lst=st.split()
    r=int(input())
    for i in range(r):
        string=rotation(lst)
    print(string)
    
def rotation(lst):
    if len(lst)<=1:
        return None
    first=lst.pop(0)
    lst.append(first)
    return lst
main()
    
    
# Define the element, number of columns, and number of rows
o = 0
cols = 4
rows = 3

# Create the 2D list
matrix = [[o] * cols for _ in range(rows)]

# Print the matrix
for row in matrix:
    print(row)
