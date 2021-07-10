# prograam for Number is Prime or Not
num = int(input("Enter a Number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number.")  
           print(i,"times",num//i,"is",num)  
           break  
       else:  
            print(num,"is a Prime Number.")  
         
else:  
   print(num,"is not a prime number")  
