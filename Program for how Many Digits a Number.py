#Program For Calculate How many Digit a Number has

Number=73968683

Digits=1
Dec=10

ExpForDigit=int(Number/Dec)

while (ExpForDigit!=0):
    Digits=Digits+1
    Dec=Dec*10
    ExpForDigit=int(Number/Dec)

print(Digits)

#-------------------------------------------------------
# Here flow is as given example
# example: we take Number=58
# Now It's 58/100 => 0.58
# Then After Here Interger part is the 0 and remaing is 58
# OK! Now Digit is 2
# It's also same flow for any Numbers
# If you Increment Numbers then Dec=Dec*10 ...in while
