inp=int(input("Enter your number here: "))
temp=inp

def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num == 1

if sum_of_digits(inp):
        print("Magic Number")
else:
     print("Not Magic number")