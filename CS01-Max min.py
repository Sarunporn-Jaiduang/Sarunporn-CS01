Num = int(input('Enter Your Loop: '))
NumTotal=[]
for i in range(Num):
    data = int(input('Enter Your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print("Maximum:",data)
print("Minimum:",data)