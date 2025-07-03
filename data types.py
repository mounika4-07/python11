#data types tells about the type of data that a variable is holding on
#data types are categorized into 5 types

#NUMBER:

#integer
a=123
print(a)
print(type(a))
print(id(a))
a1=-90
print(a1)
print(type(a1))
print(id(a1))

#float:which holds all the decimal/fractional values
#it can be represented by as float()
#code:
b=89.46
print(b)
print(type(b))
print(id(b))
b1=-93.4
print(b1)
print(type(b1))
print(id(b))

#complex:complex data types are used to real and imaginary values.
#which can be represented as a+bj.
#code:
c=9+6j
print(c)
print(type(c))
print(id(c))
c1=-10+8j
print(c1)
print(type(c1))
print(id(c1))

#2.sequence:
#sequence data type are divided into 3 types.
#a.String
#b.list
#c.tuple

#a.string:
#it is collection/group of charactres
#it can be enclosed using single quotes/double quotes 
#code:
d='ists'
print(d)
print(type(d))
print(id(d))
d1="ists"
print(d1)
print(type(d1))
print(id(d1))

#list=it is a collection ofitems/values/elements
# syntax:list name=[val1,val2,....,valn]
# code:
mylist=[10,11.8,6+5j,"hello"]
print(mylist) 
print(type(mylist))
print(id(mylist))
print(mylist[3])

#tuple:
#it is a collection of items/values/element
# syntax:tuplename=(val1,val2,....valn)
# code:
mytuple=(12,2.3,"hi",[1,2,3])
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple)

 #3.boolean:
 #it means check the condition.
 #they are divided to two ways
 #   1.true    2.flase
 #[syntax:bool] it is represented by bool
 #code:
a=True
print(a)
print(type(a))
b=False
print(b)
print(type(b))

#4.set: 
#it is a collection of values/items/elements
#syntax:setname{val1,val2,...valn}
#code:
myset={1,2.3,4+5j,"hi",("hello",5)}
print(myset)

#dictionary:it is a collection of key value pairs
#syntax: dictionaryname{key1!val1:,key2!val2:....key3!val3}
#code:
mydict={1:"ists","branch":"ece","location":"rjy"}
print(mydict)
print(type(mydict))