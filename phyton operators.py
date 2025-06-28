"""
An operator is a speacial symbol 
which is used to perform an operator
ex:c=a+b
here c,a,b,are operands
+is a speaial symbol 
"""
#the operators are:
#Arthematic operators
#elational operator
#logical operator
#bitwise operator
#identity operator
#membership operator
#assingment operator
#1 Arthematic operator:``
#Arthematic operatoris used to perform some mathematical or athematical
#the operators are +,_,*,/,//,%,**
#code:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the addition",a+b)
print("the subtration",a-b)
print("the multiplication",a*b)
print("the division",a/b)
print("the floor division",a//b)
print("the modular division",a%b)
print("the power",a**b)
#2 relatoinal/comparision operators:
   #relational operators are used to compare the values and return the boolean they are<,>,<=,>=,==,!=
#code:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the greater value ",a>b)
print("the lesser value",a<b)
print("the greater than or equal too value",a<=b)
print("the lessthan than or equal too value",a>=b)
print("the equals too values",a==b)
print("the not equals too value",a!=b)

#3 logical operators:
#logical operators are used to perform logical operations
#they are logical and,or,not
#and--if both the conditions are true it returns the true.
#T T T
#F T F
#T F F 
#F F F 
#Or--if one of the condition is true it returns the ture
#T F T
#F T T
#T T T
#F F F
#Not-- it just negotiaties the conditions
#T F
#F T
#CODE:
a=3 
b=45
c=a>=34 and b<=50
print(c)
d=67
e=89
f=d!=67 or e==89
print(f)
g=10
print(not(g)) 
h=0
print(not(h)) 
#4 bitwise operator:
#bitwise operators are used to perform binary operations they are:
#bitwise and (&):if both the bits are "1"it returns"1"
#bitwise or(|):if one of the bit is "1" it returns"1"
#bitwise xor(^):if one of the bit is "1" it returns"1"
#and if both the bits are"1" it returns"0"
#code:
a=5
b=9
c=a&b
print(c)
d=15
e=13
f=d/e
print(f)
g=12
h=14
i=g^h
print(i)
#5 membership operator:
#membership operators are used to check the values in a squence .and returns the boolen values
#they operators are "in","not in"

X=["apple","banana"]
print("apple" in X)
print("pp"not in X)
print("banana"not in X)
print("dragon"in X)
#Identity operators are used to compare the values and values and return the boolen values operators are "is","is not".
#CODE:
X = [1,2,3]
Y =[4,5,6]
Z=X
print(X is Y)
print(X is Z)
print(Y is Z)
print(Y is not Z)
print(Z is not Y)
print(X is not Y)