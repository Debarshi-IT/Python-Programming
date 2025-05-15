inp=int(input("Enter your number here: "))
temp=inp

if inp % 7 == 0 or str(inp).endswith("7"):
    print("Buzz Number")
else:
    print("Not Buzz Number")