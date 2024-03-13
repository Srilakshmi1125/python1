# task 1
# higher order function
# function that takes a s function as argument and returns a function
# def d1(para1):
#     return "d1 function", para1


# def d2():
#     return "d2 function"



# d = d1(d2())
# print(d) # ('d1 function', 'd2 function')


# task 2
# def d1(para1, para2):
    
#     return "d1 function", para1, para2

# def d2():
    
#     return "d2 function"


# def d3():
    
#     return "d3 function"


# d = d1(d2(), d3())
# print(d)  # ('d1 function', 'd2 function', 'd3 function')

# task 3
def d1(a):
    print(a)
    
    def d2(b):
        print(b)
        return a+b
    return d2

    
d = d1(10)
print(d.__name__)
print(d(20))

# task 4 closure
# a closure is a function thar remembers values in enclosing scoppes of they are not present in memory
def d1(a):
    print(a)
    
    def d2(b):
        print(b)
        return a+b
    return d2


d = d1(10)
# print(d.__name__)
# print(d(20))

del d1 

# d1(100)  # NameError: name 'd1' is not defined. Did you mean: 'd'?
print(d(200))