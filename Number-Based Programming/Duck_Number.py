inp=int(input("Enter your number here: "))
temp=inp
flag=0
for i in range(len(str(inp))-1):
    if(temp%10==0):
        flag=1
    temp=temp//10
 
    flag=0
   
if(flag==1):
    print("Condition met for Duck number!")
else:
    print("Condition not met for Duck number!")