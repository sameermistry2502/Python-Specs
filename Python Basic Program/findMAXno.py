N = input('Size of Array')

Arr=list()

for list in range(0,int(N)):
    temp=int(input('Enter the array:'))
    Arr.append(temp)

maxn=Arr[0]

for i in range(1,int(N)):
    if (maxn<Arr[i]):
        maxn=Arr[i]

print(maxn)
