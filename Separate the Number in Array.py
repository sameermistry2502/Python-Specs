#Program For Separate a number and saved into Array
Number=7359419146

Digits=1
Dec=10

ExpforDigits=int(Number/Dec)

while (ExpforDigits!=0):
    Digits=Digits+1
    Dec=Dec*10
    ExpforDigits=int(Number/Dec)

print(Digits)
#--
print(Dec)
#----
Dec=Dec/10

fArray=list()

while (Dec!=0.1):
    Temp=int(Number/Dec)
    fArray.append(Temp)

    Number=Number-Temp*Dec
    Dec=Dec/10

print(fArray)
#----------------------------------------------------------
# For that Analysis understanding you need to under stood previous program i.e calculate number then gives digit
# In this up to -- is same scenario as we can saw in previous program
# Divide the DEC by 10(Make New Dec value)i.e Dec=Dec/10
# make list { i.e[fArray] }in our program
# AS per while loop works up to Dec=0.1
# If while loop is Dec!=0.1 then
# Store the Expression value in temporary variable i.e Temp=int(Number/dec)
# Now append temp data in fArray
# Number=Number-Temp*Dec (Here Dec is 100)
# AS per our Program How it's work:
# 7359419146=7359419146-7*1000000000 [Answer is 359419146]
# It's works up to while condition has false
# Repeateadly divided Dec i.e Dec=Dec/10 .... {Line No 27}
# print the fArray
