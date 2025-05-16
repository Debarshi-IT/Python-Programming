inp=int(input("Enter your number here: "))
temp=str(inp)

a=0
for i in range(len(temp)):
    a+=int(temp[i])**(i+1)
if a==inp:
    print("Disarium number")
else:
    print("Not Disarium Number")