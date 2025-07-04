"""Tuples is a collection items/value/values
they are enclosed within the parenthesis or open brackets () by {}
as tuple are immutable it mean  we can't change so when the data is fixed we can go with tuple 

"""

mytuple = (13,12,11)
print(type(mytuple))#<class tuple>
mytuple2=()#empty tuple
print((mytuple2))#<class tuple>
mytuple3=(10)
print(type(mytuple3))#<class int>

"""
note:when you wanna create a tuple with single value
it should be separated by so that the complier
treats as tuple or else it just treats integer
"""
#syntax:tuplevariable=(val1,val2,val3,..valn)
mytuple5=(12,23,45,34+78j,[12,34,45],"hello",(123,"ece"))
mytuple6=(45,)
print(type(mytuple6))
#creating the tuple with a single element
t=[23,45,56,"jj"]
print(t)
k=(tuple)
print(k)
#creating the tuple with "tuple" predefined word 
t=tuple()#it consider as a empty tuple
print(t)