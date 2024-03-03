# Function with our arguments
def d1():
    
    print("d1 function")
 
d1()   #d1 function

# function with args
def d2(a, b):
    
    print(a, b)
    

d2(10, 20) #10 20 


# function with default values
def d3(a = 100, b = 200):
    
    print(a, b)

d3(20, 40) #20 40

# function using key and values 
def d4(a, b):
    
    print(a, b)
    
d4(a=100, b= 120) #100 120

# function using arbitrary *args
def d5(*colors):
    print(colors)

d5("red","green")    #('red', 'green')

# function with **kwargs
def d6(**colors):
    
    print(colors)
    
    
d6(first_color="green", second_color="white", third_color="yellow") #{'first_color': 'green', 'second_color': 'white', 'third_color': 'yellow'}

# function using return keyword
def d7():
    
    return "Hello world!"


d = d7()
print(d)  # Hello world!

def d8(a,b):
     
     return a*b

d = d8(3,4)
print(d)   # 12

# nested functions
def d9(firstname):
    
    def d10(lastname):
        
        print(firstname + " " + lastname)
        
    d10("Kiran")
    
d9("Sai")  #Sai Kiran

def d11(Name):
    
    def d12(Surname):

        print(Name + "" + Surname)

        
    d12("Natte")

d11("Srilakshmi")

    




   