#program for swap two numbers using some techniques
print('Using C Programing technique to swap two Numbers')
s = 73
m = 96

print("s is:",s,'and','m is:',m)
temp = s
s=m
m=temp
print('s is:',s,'and','m is:',m)
#------------------------------------

#Another technique to swap the numbers
print('By Using Addition/Subtraction to swap the Number')
s1 = 83
m1 = 96

print("s1 is:",s1,'and','m1 is:',m1)
s1 = s1+m1 # 83+96 =  179
m1 = s1-m1 # 179-96 =  83
s1 = s1-m1 # 179-83 = 96
print('s1 is:',s1,'and','m1 is:',m)
#--------------------------------------

# PYTHON TECHNIQUE

print('Python technique for swap two numbers')

sm = 83
ms = 81

print("sm is:",sm,'and','ms is:',ms)
sm,ms = ms,sm  # In one line logic for swap Values 
print('sm is:',sm,'and','ms is:',ms)

#------------------------------------------

