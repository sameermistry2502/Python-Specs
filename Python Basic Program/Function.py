Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def studentDetails(rollno,name,branch,collage):
	print("Roll no is:"+rollno + "Name is "+name + "Branch is"+branch + "Collage is"+collage)

	
>>> studentDetails(12,"sameer","IT"."ASOIT")
SyntaxError: invalid syntax
>>> studentDetails(15,"sameer","IT","ASOIT")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    studentDetails(15,"sameer","IT","ASOIT")
  File "<pyshell#2>", line 2, in studentDetails
    print("Roll no is:"+rollno + "Name is "+name + "Branch is"+branch + "Collage is"+collage)
TypeError: Can't convert 'int' object to str implicitly
>>> studentDetails("15","sameer","IT","ASOIT")
Roll no is:15Name is sameerBranch isITCollage isASOIT
>>> def studentDetails(rollno,name,branch,collage):
	print("Roll no is:"+rollno + "\nName is "+name + "\nBranch is"+branch + "\nCollage is"+collage)

	
>>> studentDetails("14","preyas","IT","ASOIT")
Roll no is:14
Name is preyas
Branch isIT
Collage isASOIT
>>> studentDetails("15","MISTRY SAMEER B","Information Technology","Aditya Silver Oak Institute Of Technology")
Roll no is:15
Name is MISTRY SAMEER B
Branch isInformation Technology
Collage isAditya Silver Oak Institute Of Technology
>>> 
