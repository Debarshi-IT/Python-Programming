import math

inp=int(input("Enter your number here: "))
temp=inp
l=len(str(inp))
if (l%2!=0):
    quit()
if(((inp//(10**(l/2)))+inp%(10**(l/2)))**2)==inp:
    print("Tech Number")
else:
    print("Not Tech Number")