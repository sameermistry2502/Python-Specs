Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> email ="sameermistry2502@gmail.com"
>>> password ="sam1234"
>>> if email == "sameermistry2502@gmail.com":
	print("welcome "+email)
	if password == "sam1234":
		print("welcome :"+email)
	else:
		print("Incorrrect password!")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if email == "sameermistry2502@gmail.com":
	if password == "sam1234":
		print("welcome :"+email)
	else:
		print("Incorrrect password!")
else:
	print("Incorrect Email-Address")

	
welcome :sameermistry2502@gmail.com
>>> if email == "sameermistri2502@gmail.com":
	print("welcome "+email)
	if password == "sam1234":
		print("welcome :"+email)
	else:
		print("Incorrrect password!")
else:
	print("Incorrect Email Address Please Check!")

	
Incorrect Email Address Please Check!
>>> 
