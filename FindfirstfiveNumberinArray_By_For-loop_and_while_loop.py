
sameer=[255,3666,22,55,44,77,88,15,96]
#-----------------Using For loop------------------------
N=len(sameer)

FinalNumber=5

Approved=list()

for I in range(0,N):
    if (sameer[I]>25 and FinalNumber>0):
        Approved.append(sameer[I])
        FinalNumber=FinalNumber-1

print(Approved)

#-----------------Using while loop---------------------------

FinalNumber=5


Approved2=list()

I=0
while (FinalNumber>0):
    if(sameer[I]>20):
        Approved2.append(sameer[I])
        FinalNumber=FinalNumber-1
    I=I+1

print(Approved2)

#-------------------------------------------------------
# Now Here both loop perform simantanausaly
# OUTPUT will be given same
# BUT
# for loop performs 13 times from sameer list
# while loop performs 8 times
# SO while loop reduces performace over Machine
