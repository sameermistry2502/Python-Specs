Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(a,b):
	print(a+b)

	
>>> add(12,12)
24
>>> def add1(p,q):
	print(p+q)

	
>>> add1(7,8)
15
>>> def addval(v1,v2):
	return v1+v2

>>> addval(9,9)
18
>>> add(10,12)*3
22
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    add(10,12)*3
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> addval(46,46)*2
184
>>> #local variable
>>> def deffun():
	a1 = 10
	a2 = 10
	print(a1+a2)

	
>>> deffun()
20
>>> print(a1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(a1)
NameError: name 'a1' is not defined
>>> #globle variabls
>>> s1 = 15
>>> s2 = 16
>>> def addsum()
SyntaxError: invalid syntax
>>> def addsumm():
	print(s1+s2)

	
>>> addsumm()
31
>>> print(s1)
15
>>> print(s2)
16
>>> 
