# set 
# set is unordered elements 
# list and tuple are ordered elements
# set will not maintain duplicates, list and tuple will maintain duplicates
# set is mutable, frozen set is immutable
# s1 = set()
# print(s1)
# s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
# print(s1) # {50, 20, 70, 40, 10, 60, 30}
# methods : add', 'clear', 'copy', 'discard', 'pop', 'remove', 'update'

# add :
# s1={"sri"}
# s1.add("lakshmi")
# print(s1) # {'sri', 'lakshmi'}

# remove :
s1={10,20,30,40,10,20}
s1.remove(10)
print(s1) # {40, 20, 30}

# discard :
s1={10,20,30,40,10,20}
s1.discard(20)
print(s1) # {40, 10, 30}

# update :
s1={10,20,30,40,10,20}
s1.update([40,50])
print(s1) # {40, 10, 50, 20, 30}

l1=list(s1)
print(l1) # [40, 10, 50, 20, 30]

l1.sort()
print(l1)  # 10, 20, 30, 40, 50]

f1 = frozenset()
print(f1) # frozenset()

s1 = set()
s1.add(f1)
print(s1) # {frozenset()}

s1 = {10, 20, 30, 40}
print(s1)

f2 = frozenset(["NameOne", "NameTwo"])
s1.add(f2) # 
print(s1)  # {40, 10, frozenset({'NameOne', 'NameTwo'}), 20, 30}

s1.remove(f2)
print(s1)  # {40, 10, 20, 30}

