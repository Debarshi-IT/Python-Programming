inp=int(input("Enter your number here: "))
temp=inp

def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


digit_sum = sum(int(digit) for digit in str(inp))
if inp % digit_sum == 0 and sum_of_digits(digit_sum) == 1:
    print("Harshad Magic Number")
else:
    print("Not Harshad Magic Number")
