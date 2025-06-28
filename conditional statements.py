"if"
"""
if condition:
    statements
"""
#write a python program to find whether a number is positive or not

num=int(input("enter a number.."))
if num>0:
    print("the number is positive",num)

#write a program to find biggest of two numbers

a=int(input("enter a number:"))
b=int(input(" enter a number:"))
if a>b:
    print("A is greater:",a)
else:
    print("B is greater:",b)

#Accept the percentage from the user and disply the grade according to the following criteria
"""
BelowD -25
25 to 45 -- C
45 to 50 -- B
50 to 60--B+
60 to 80---A
Above 80+--A+
"""

pr =int(input("enter your percentage.."))
if pr<=25:
    print("The grade is D ..")
elif pr>=25 and pr<=45:
    print("The grade is c..")
elif pr>=45 and pr<=50:
    print("the grade isB..")
elif pr>=50 and pr<=60:
    print("The grade is B+..")
elif pr>=60 and pr<=80:
    print("The grade is A..")
elif pr>=80:
    print("The grade is A++..")
else:
    print("Your are failed..")

#write a program to display the week names by taking input from user
day =int(input("enter  your week name:"))                 
if  day==1:
    print("sunday")
elif day==2:  
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday") 
elif day==5:
    print("thursday") 
elif day==6:
    print("friday")  
elif day==7:
    print("saturday")                      
