inp=int(input("Enter your number here: "))
temp=inp

for i in range(1, inp):
    if i * (i + 1) == inp:
        print("Pronic Number")
        break
