"""
Nested if : A if within a if is called Nested if
syntax; if condition:
                0uter if statement
                 if condition:
                    inner if statements
                 else:
                    inner else statements
        else:
            outer else statements
"""
is_snowing=True
temp=int(input("enter the temperature.."))
if is_snowing>10:
    print("please carry umbrella..")
    if is_snowing==-10:
        print("please carry umbrella and jacket")
    else:
        print("enjoy the sunny day!!")
else:
    print("enjoy ur day")


#Exprees delivery
weight=int(input("enter the weight"))
if weight==4:
    print("the delivery can be expected within 24 hrs..")
    if weight<=10:
        print("need to pay an extra amount for extra weight..")
    else:
        print("no need to pay any extra charge have a great delivery !!")
else:
    print("need to wait 3-5 bussiness days to expect the delivery")

    