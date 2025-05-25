inp=int(input("Enter your number here: "))
temp=inp
Sum=0
Prod=1
for i in range(len(str(inp))):
    Sum+=temp%10
    Prod*=temp%10
    temp//10
if (Sum==Prod):
    print("It is a Spy Number!")
else:
    print("It is not a Spy Number!")