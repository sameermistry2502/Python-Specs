arr=[25,11,4,11,552,2]

N=len(arr)

print(N)

for J in range(0,N-1):
 for I in range(0,N-J-1):
     if (arr[I]<arr[I+1]):
         Temp=arr[I]
         arr[I]=arr[I+1]
         arr[I+1]=Temp

print(arr)
