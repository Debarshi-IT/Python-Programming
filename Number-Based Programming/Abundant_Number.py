inp=int(input("Enter your number here: "))
temp=inp

if sum(i for i in range(1, inp) if inp % i == 0) > inp:
    print("Abundant number")
else:
    print("Not Abundant number")