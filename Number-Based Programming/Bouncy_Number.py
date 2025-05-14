inp=int(input("Enter your number here: "))
temp=inp

def is_mixed(num):
    digits = [int(digit) for digit in str(num)]
    increasing = all(digits[i] < digits[i+1] for i in range(len(digits) - 1))
    decreasing = all(digits[i] > digits[i+1] for i in range(len(digits) - 1))
    return not increasing and not decreasing
if is_mixed(inp):
    print("Bouncy Number")
else:
    print("Not Bouncy Number")