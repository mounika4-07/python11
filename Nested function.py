#Nested function:a function with in a function is called Nested functions
def outerfunction():
    print("outerfunction statement")
    def innerfunction():
        print("innerfunction statement")
    innerfunction()
outerfunction()

        
        
        
        
