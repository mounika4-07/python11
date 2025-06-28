#if a==10:
#print("the if statement is executed")
#Accept the number of days from the user and culculate  charge the libary

num =int(input("enter the day"))
if num<=5:
    print("the charge is..",num*2)
elif num>=6 and num<=10:
    print("the charge is..",num*3)
elif num>=11 and num<=15:
    print("the charge is ..",num*4)
elif num<=15:
    print("the chargeis..",num*5)
else:
    print("wrong days selected")

"""
 write a program to accept two numbers from user and an operator and perform operation accordingly
 num1 : 5 
 num2 :10 
 opr : +
 answer : 1 
"""
num1 =int(input("enter a number"))
num2 =int(input("enter a number"))
opr =  input("enter a operator:")
if opr=="+":
    print("the amswer:",num1+num2)
elif opr=="-":
    print("the answer:",num1-num2)
elif opr=="*":
    print("the answer:",num1*num2)
elif opr=="/":
    print("the answer:", num1/num2)
else:
    print("wrong operator selected..")

"""
write a program to accept anumber from 1 to 12 then display name of the  month and days in the month like 1 for january and the no of days
and so on
"""
month=int(input("enter a month number"))
if month==1:
    print("jan:,31")
elif month==2:
    print("feb:,28")
elif month==3:
    print("mar:,31")
elif month==4:
    print("apr:,30")
elif month==5:
    print("may,31")
elif month==6:
    print("jun:,30")
elif month==7:
    print("jui,31")
elif month==8:
    print("aug:,30")
elif month==9:
    print("sep,31")
elif month==10:
    print("oct:,30")
elif month==11:
    print("nov:,30")
elif month==12:
    print("dec:,31")
else:
    print("wrong nubmer")                                    