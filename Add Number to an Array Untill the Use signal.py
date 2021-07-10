#Program for aading numbers in Array Untill the USER'S SIGNAL

Enroll=list()

N=int(input('Enter the E Number :'))

while (N!=96):
    Enroll.append(N)

    N=int(input('Enter again plz: '))

print(Enroll)

#----------------------------------------------------------------
# Here we can understand flow of code by Example
# Example : 1.Frist user can enter the stream Number i.e = 11,15,33,14,34,27,23,26
# 2.provided one key value i.e = 96
# 3.If user can enter key i.e = 96 then stop process and append all in list(Array)
# Now Key indicates User's Signal means stop adding and then after print list
