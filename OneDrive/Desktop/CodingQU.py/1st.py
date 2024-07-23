#You are given a number N and you have to print the given pattren
#for N=3  
#333222111
#332211
#321
line=3
for i in range(line, 0, -1):
    for j in range(line, 0, -1):
        print(str(j) * i, end='')
    print()