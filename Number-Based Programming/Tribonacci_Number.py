inp=int(input("Enter your number here: "))
temp=inp

series=[0,1,1]
for i in range(1000):
    series.append(series[-1]+series[-2]+series[-3])
if inp in series:
    print("Tribonacci Number")
else:
    print("Not Tribonacci Number")