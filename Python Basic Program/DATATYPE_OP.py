Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "sameer"
>>> college = "ASOIT"
>>> semester = 5
>>> PER YEAR FEES FOR BE = 63000.0
SyntaxError: invalid syntax
>>> per_year_fees = 63000.0
>>> type(per_year_fees)
<class 'float'>
>>> type(name)
<class 'str'>
>>> Ename,Eage,Esalry = "sameer",19,19000.0
>>> print(Eage)
19
>>> print(Esalary)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(Esalary)
NameError: name 'Esalary' is not defined
>>> print(Esalary)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(Esalary)
NameError: name 'Esalary' is not defined
>>> print(Esalry)
19000.0
>>> print(Ename)
sameer
>>> date
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    date
NameError: name 'date' is not defined
>>> date = 12/12/2017
>>> type(date)
<class 'float'>
>>> date
0.0004957858205255329
>>> date = "15-02-2017"
>>> date
'15-02-2017'
>>> faculties = ["Archana Gondalia","Manjula Singh","Jalpa Shah","Jaysree Upadhyay","Manish Singh","DushyantSingh Rathod"]#List in Python
>>> Branch = ("CE/IT DEPARTMENT",16,07)#Tuple in python
SyntaxError: invalid token
>>> Branch = ("IT DEPARTMENT",16)#Tuple in Python
>>> H_O_D = {"IT":RAHUL_SRIMALI , "CE":SAGAR_PATEL}
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    H_O_D = {"IT":RAHUL_SRIMALI , "CE":SAGAR_PATEL}
NameError: name 'RAHUL_SRIMALI' is not defined
>>> HOD = {"IT":"RAHUL SRIMALI","CE":"SAGAR PATEL"}
>>> print(facilties)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(facilties)
NameError: name 'facilties' is not defined
>>> faculties
['Archana Gondalia', 'Manjula Singh', 'Jalpa Shah', 'Jaysree Upadhyay', 'Manish Singh', 'DushyantSingh Rathod']
>>> HOD
{'CE': 'SAGAR PATEL', 'IT': 'RAHUL SRIMALI'}
>>> Branch
('IT DEPARTMENT', 16)
>>> faculties[1]
'Manjula Singh'
>>> faculties.append("Namita Patel")
>>> faculties
['Archana Gondalia', 'Manjula Singh', 'Jalpa Shah', 'Jaysree Upadhyay', 'Manish Singh', 'DushyantSingh Rathod', 'Namita Patel']
>>> faculties [1:]
['Manjula Singh', 'Jalpa Shah', 'Jaysree Upadhyay', 'Manish Singh', 'DushyantSingh Rathod', 'Namita Patel']
>>> faculties [0:4]
['Archana Gondalia', 'Manjula Singh', 'Jalpa Shah', 'Jaysree Upadhyay']
>>> fac2 = ["Nipa Patani","Vidhi Patel"]
>>> AllFaculty = faculties+fac2
>>> AllFaculty
['Archana Gondalia', 'Manjula Singh', 'Jalpa Shah', 'Jaysree Upadhyay', 'Manish Singh', 'DushyantSingh Rathod', 'Namita Patel', 'Nipa Patani', 'Vidhi Patel']
>>> 
