from random import randint

List = list()
N=int(input('Enter size of the list:'))

for e in range(0,N):
    temp=randint(0,10)
    List.append(temp)

print(List)
