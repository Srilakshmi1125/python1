# list 
# List is a datatype and it is an object 
# List is unsafe (muttable)
# In list we can store different types of datatypes 
# List will maintain the insertion order 
# List will allow duplicates values 
l=[]
print(type(l)) # <class 'list'>

# index call
# l=[1,2,4,66,77]
# print(l[3]) # 66

# slicing :

l=[1,2,4,66,77]
# syn for slicing:[start:stop:skip]
print(l[0:3:2]) # [1, 4]

# list methods : append, extend, count, pop, remove, insert

# append(element) : adds only one element at the end of the list

# l1=[]
# l1.append(10)
# print(l1) # [10]

# l2=[]
# l2.append(10,20,30)
# print(l2) # TypeError: list.append() takes exactly one argument (3 given)

# l3=[]
# l3.append(20)
# l3.append(30)
# print(l3) # [20, 30]  

# Two behavioiurs:
# extend(string element)
# extend([elements])

# l4=[1,2,3,4]
# l4.extend("srilakshmi") # [1, 2, 3, 4, 's', 'r', 'i', 'l', 'a', 'k', 's', 'h', 'm', 'i']
# print(l4)

# l5=[22,33,44]
# l5.extend([55])
# print(l5) # [22, 33, 44, 55]

# Two behavioiurs:
# pop() : delete the last element 
# pop(index) : delete the index element

# l6=[1,2,3,34,55]
# l6.pop(2)
# print(l6) # [1, 2, 34, 55]

# insert(index, element)

# l7=[1,2,4,5,7]
# l7.insert(3,'sri')
# print(l7) # [1, 2, 4, 'sri', 5, 7]

# remove(element)

l7=[1,2,4,5,7]
l7.remove(4)
print(l7) # [1, 2, 5, 7]

# clear()


# copy()
l1 = [10, 20, 30, 40]
print(l1)  # [10, 20, 30, 40]
print(l1.copy()) # [10, 20, 30, 40]

# reverse()
l1 = [10, 20, 30, 40]
l1.reverse()
print(l1)  # [40, 30, 20, 10]

# sort()
l1 = [50, 30, 10, 20, 10]
l1.sort(reverse=False)
print(l1)  # [10, 10, 20, 30, 50]

l1.sort(reverse=True)
print(l1)  # [50, 30, 20, 10, 10]
