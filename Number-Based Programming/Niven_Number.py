inp=int(input("Enter your number here: "))
temp=inp

if inp % sum(int(digit) for digit in str(inp)) == 0:
    print("Niven Number")
else:
    print("Not Niven Number")