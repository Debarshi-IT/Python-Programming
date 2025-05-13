inp=int(input("Enter your number here: "))
temp=inp

digits = str(inp)
if sum(int(digit) ** len(digits) for digit in digits) == inp:
    print("Armsrong number")
else:
    print("Not Armsrong number")