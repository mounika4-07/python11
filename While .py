"""""
looping statements are also called as iterative statements
These statements are used to run a particular condition
no.of time ..divided into 2 types
1.while
2.for
"""
#while:it executes when the condition is true
"""
syntax:while condition:
            statemates
            exit condition/incrementation
"""
#eg:
i =1
while i<=10:
    #print(i)-->in this particular line the
    #"i"value runs "n" times because no incrementation/exit cond specification"
    print("the valve",i)
    i+=1

#eg2:
while True:
    print("the while condition")
#note: As default condition is true the while loop "infinity"times


#eg3:
while False:
    print("the while condition")
#As while is also called entry control
#  loop it just checks the condition in the entrance
# as default flase is given as condition it wont execute    