BinaryNumber=[1,1,1,1,0]

N=len(BinaryNumber)

initNo=0

for I in range(0,N):
  initNo=initNo+BinaryNumber[I]*(2**I)
  
print(initNo)