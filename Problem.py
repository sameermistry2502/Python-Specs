import math

stu=list()

N=int(input('Enter the no'))
print(N)

for x in range(1,N+1):
  Fx=(x*2*2)/math.sqrt(x)
  stu.append(Fx)
  
print(stu)