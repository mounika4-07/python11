"""
String:- string is a collection of characters and a character is asimple a symbol for example 
the english language has 26 characters and computer don't deel with characters a deel with binary numbers 
even now you may see characters on sreen internally ,it's stored and manuplated as a combination "0" and "1"
"""
#string element as a access the 
#string element can be using the indexing and the silcing
a="mounika yesulanka"
print(a[0:8])
print(a[0:16:9])

#representation of a string:-3 ways
#(''),("" ""),(""" """")
v='IT'
print(type(v))

v2="ECE"
print(type(v2))

v3="""abc"""'s'
print(type(v3))

#string methods:-
#syntax:converts form lower to upper case
#1.upper():converts form lower to upper case
w="python"
print(w.upper())

#2.lower():converts from upper to lower case 
w2="python"
print(w2.lower())

"""
Count method:-
this method is used to count the repeated words in a string
"""
m="i love mounika mounika "
print(m.count ("mounika"))
"""
index method:
this method is used to return the index position of a string.
"""
n="mounika yesulanka"
print(n.index("u"))
"""
strip:-
this method is used to remove the spaces in the string.
"""
s1="this is my book "
print(len(s1))
print(s1)
s2=s1.strip()
print(len(s2))
print(s2)

s1=" this is my book "
print(len(s1))
print(s1)
s2=s1.rstrip()
print(len(s2))
print(s2)
"""
#format function:-this method is used to return the string in a automated/realformat
"""
names=["pandu","varun","ganesh","sati"]
for i in names:
    print("hi {} tinava?".format(i))

#FIND METHIOD:-this method is used to returns the -1 when the string element is not present 
n="MOUNIKA"
print(n.find("K"))
print(n.find("I"))

#STARTSWITH(): when the string is starts with given string it returns true,
#it returns to when the string starts with given string  with existing string
n = "I LOVE YOU"
print(n.startswith("I"))

#ENDSWITH():
m="SRIMANNARAYANA YESULANNKA"
print(m.endswith("A"))

# REAL TIME APPLICATION CO0DE:
websites=["amzon.com","myntra","ojio.in",]
in_websites=[]
for  i in websites:
     if i.endswith(".in"):
         in_websites.append(i)
print(in_websites)     

#ISALPHA:it checks  if the all the character is string are alphabets are not return the boolean values.
#w1="python"
#print(w1.lower())
print("openai".isalpha())
print("openai123".isalpha())
print("open ai".isalpha())

#IS ALNUM():checks if all characters in a string  are alpha numric i.e numbers or letters
print("openai123".isalpha())#flase
print("openai123".isalnum())#true
print("openai!".isalnum())#flase
print("openai123".isalnum())#true

#TITTLE():it just returns the given string tittle format
#title():
m="the wings of five"
print(m.title())

#SPLIT(): it slipt the given string into spilt
a="hello"
print(a.split())

#join():it joins the spilted list into  the string
s1="  ".join(a)
print(s1)








