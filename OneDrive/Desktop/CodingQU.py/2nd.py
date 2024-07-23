# you have been given an array of integers. you task is to write a program
#sort the elements such that all even elements apperar first, fallowed by all
#odd elements. while maintaining relative order of even and odd elements.
#implemnt the sorting algo inplace
n=int(input())
A=list(map(int,input().split()))
even=[]
odd=[]

for num in A:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even+odd)
       