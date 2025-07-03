"""
list is a coolection/group of items/values/elements
they can be enclosed within the square bracket[]seperated by(,)
listmethods:append/extend/count/mutability index/remove/pop/insert
syntax:listname.methodname()
"""
#append:this method id uded to add the elements

list1=["edinburg","scotland","london"]
print(list1)
list1.append("bhrinimgam")
print(list1) 

#extend:this method is used to add the elements at the end but
#as a sublist
list1.extend(["paris","malta","aus"])
print(list1)
#count:this method count the mumber of repeated elements in a list
flowers=["rose","mary","rose","jasmine","hibiscus"]
flowers.count("rose")
print(flowers)


#mutability:changing the elements
mylist4=["hello","ece",123,34.56,56+78j]
print(mylist4)
mylist4[2]="agri"
print(mylist4)

#pop..removes the elements using index
mylist5=[12,34,565,78.9,34+56j,"hello"]
print(mylist5)
mylist5.pop(2)
print(mylist5)

#remove...removes the elements directly
mylist5.remove(34)
print(mylist5)

#count--it counts the number of accurance
#of a item in alist
mylist6 = [22,33,33,22,55,32,22,44,67,56,22]
print(mylist6.count(22))