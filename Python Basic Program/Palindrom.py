# Program for palindrom or not
#-----------Check the entered value Palidrom or Not----------------------

M = input("Enter the Value:->")

rev = M[::-1]#In built Python Provided for reverse String

if M == rev:
    print ('Input: {},Rev: {}'.format(M,rev))#print variable Index Value
    print ("It's a Palindrom String")
else:
    print ('Input: {},Rev: {}'.format(M,rev))#print Variable Index value
    print("It's Not Palindrom.")

#------------Anthor Menhod ---------------------------------------------
'''
my_str = input('Enter the String:')

# reverse the string
rev_str = reversed(my_str)#Another way to String Reverse

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
'''

#-----------------------------------------------------------------------
