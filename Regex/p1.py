# Task 1:
import re
string = 'MyIds_101'
pattern = r'\w'
m = re.match(pattern,string)
x = m.group()
print(x)  # M

# Task 2
# string = 'MyIds_101'
# pattern = r'\w+'
# m = re.match(pattern,string)
# x = m.group()
# print(x)  #  MyIds_101

# Task 3:
# string = '@@@MyIds_101__'
# pattern = r'\w+'
# m = re.match(pattern,string)
# x = m.group()
# print(x)

# Task 4:
import re

string = "SriLakshmi@gmail.com"
pattern = r'(\w+)@(\w+)\.(\w+)'
m = re.match(pattern, string)
x = m.group(0)
print(x)  # SriLakshmi@gmail.com
print(m.group(1))  # SriLakshmi
