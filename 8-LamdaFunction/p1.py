# Lambda functions are similar to user-defined functions but without a name
# expressions that are usually a single line of a statement

# task1
# without lambda
def d1():
    
    return print("Hello World")  # Hello World
d1() 

# # with lambda
# # lambda arguments : exprerssions
d2 = lambda: print("Hello World")
print(type(d2))  # <class 'function'>
d2()  # Hello World

# task 2
# def d1(a):
    
#     return print(a)   # 10
 
# d1(10)

# # lambda arguments : exprerssions
# d2 = lambda a : print(a)
# d2(10)

# task 3
# def d1(a, b):
    
#     return print(a+b)   # 30
 
# d1(10,20)

# # lambda arguments : exprerssions
# d2 = lambda a, b : print(a + b)
# d2(10, 20)   # 30

# task 4
# r1 = lambda a, b = 5: print(a+b)
# r1(10)

# r1 = lambda a = 5, b = 10: print(a+b)
# r1()

def d1(a):
    
    def d2(b):
        
        return print(a + b)
    
    return d2 


d = d1(10)
d(5)


r1 = lambda a : (lambda b : print(a+b))
r = r1(10)
r(5)