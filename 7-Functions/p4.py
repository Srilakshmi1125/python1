# decorators : allows you to modify or extend the behavior of functions or methods without changing their actual code.
# task 1
# def d1(func):
    
#     return print(func)  # Hello Py

# d1("Hello Py")

# d = d1 
# print(d)  # <function d1 at 0x104158c20>
# print(d.__name__)  # d1
# d("Hello Python")

# task 2
# def d1(func):
#     def d2():
#         return "Hi", func()
#     return d2


# def d3():
    
#     return "Hello Python"

# # manually
# d = d1(d3)
# print(d)  # <function d1.<locals>.d2 at 0x102e7c7c0>
# print(d.__name__)  # d2
# print(d())  # ('Hi', 'Hello Python')

def d1(func):
    
    def d2(username, password):
        
        return "User Name and Password is: ", func(username, password)
    
    return d2 

@d1
def d3(uName, pWord):
    
    return uName, pWord

d = d3("Sai", "Kiran")
print(d)