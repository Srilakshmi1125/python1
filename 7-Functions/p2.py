# globals()
# syntax: globals()[str]

# # task 1
# x = 10
# def d1():
    
#     x = 20
#     print("Global variables: ", globals()["x"])  # Global variables:  10
#     # print("Local variables: ", x)  # Local variables:  20
    

# d1()

# # task 2 : locals()[str]
# # locals()
# def d2():
    
#     x = 20
#     print("Local variables: ", x)  # Local variables:  20
#     print("Local variables: ", locals()["x"])   # Local variables:  20
#     locals()["x"] = 30
#     print("Local variables: ", locals()["x"])   # Local variables:  20
     
# d2()

# locals()["x"] = 40
# print("Local variables: ", locals()["x"]) # Local variables:  40
# print("Local variables: ", locals()["x"])

# #task 3 : using return keyword for both locals() and globals()
# x,y, z = 40, 50, 60

# def g():
    
#     return globals()

# def l():
#     a, b, c = 10, 20, 30 
#     return locals()

# print(g())
# print(l())

# task 5: global keyword

x = 10
def d4():
    
    global y
    y = 20
    print(x)
    print(y)
    

d4()

print(x)
print(y)


# task 6: assigning a function to a variable
def d1(a, b):
    
    print(a + b)  # 15
    
    
c = d1
c(5, 10)  
print(type(c)) #<class 'function'>

# task 7: inner function
def d1():
    print("d1 function")
    def d2():
        print("d2 function")
    d2()


d1()

# task 8: inner function with arguments
# def d1(a):
#     print(a)  # 10
#     def d2(b):
#         print(b)  # 5
#         print(a+b) # 15
#     d2(5)


# d1(10)

# task 9: inner function with arguments
# def login():
    
#     def sales():
#         print("sales login")
        
#     sales()
    
#     def support():
#         print("support login")
        
#     support()
    
#     def developers():
#         print("developers login")
        
#     developers()
    
    
# login()