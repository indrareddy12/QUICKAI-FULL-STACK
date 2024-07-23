#write a function that takes a string as input , counts the number of lowercase and
#uppercase characters the entire string converts into the case with greater count.
#if count is equal leave the string unchanged.
#eg. MAdam
#madam

def convert(input_str):
    lower=sum(1 for char in input_str if char.islower())
    upper=sum(1 for char in input_str if char.isupper())
    
    if lower>upper:
        return input_str.lower()
    elif upper>lower:
        return input_str.upper()
    else:
        return input_str
    
st=input()
print(convert(st))