# if 

# Syntax: 
# if condition:
   
#    logic
# else:
#     logic

# what is unreachable code 
# when we pass boolean default values as condition we can see unreachable code
 
#task 1
if True:
    print("Hello world!")
else:
    print("iam in") #Hello world!

# task 2
x=5
if x%2==0:
    print("Even Number")
else:
    print("odd number")

# input() and eval()
# if, else, elif

# task 3 
a=2
b=5

if a>b:
    print("its true")    
else:
    print("its false")  # its false

# task 4
    
# username = input("Enter username:")
# password = input("Enter password:")

# if username == "admin" and password == "admin":
    
#      print("Login Successfully")
    
# else:
    
#      print("Login Failure")

# task 5
# a=5
# b=7
# c=8
# # # when we use "and" operator it must satisfy both the conditions
# if a == b and c == a:
    
#    print("if condition")
    
# else:
    
#     print("else condition")  # else condition

# task 6:
# elif : 
# Not for Interview: elif can be also called ladder condition
     
emp_salary = float(input("Enter your salary: "))

if emp_salary <= 30000:
    print("No Tax Deductions")
elif  emp_salary <= 40000:
    print("Tax Deductions")
elif  emp_salary <= 50000:
    print("Tax Deductions")
elif  emp_salary <= 60000:
    print("Tax Deductions")
elif  emp_salary <= 70000:
    print("Tax Deductions")
else:
    print("Invalid Data")

    
