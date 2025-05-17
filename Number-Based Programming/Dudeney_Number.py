inp=int(input("Enter your number here: "))
temp=inp

if round(inp** (1/3)) ** 3 == inp and sum(int(digit) for digit in str(inp)) == round(inp ** (1/3)):
    print("Dudeney Number")
else:
    print("Not Dudeney Number")