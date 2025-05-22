inp=int(input("Enter your number here: "))
temp=inp

if sum(int(digit) for digit in str(inp ** 2)) == inp:
    print("Neon Number")
else:
    print("Not Neon Number")