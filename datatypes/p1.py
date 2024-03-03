i = 10
print(i, type(i))  # 10 <class 'int'>
j = 10.0
print(j, type(j)) # 10.0 <class 'float'>

b = True
print(b, type(b)) # True <class 'bool'>

c = 10j
print(c, type(c)) # 10j <class 'complex'>

s = "hello"
print(s, type(s)) # hello <class 'str'>

l1 = []
print(l1, type(l1))  # [] <class 'list'>

t1 = ()
print(t1, type(t1))  # () <class 'tuple'>

r1 = range(0)
print(r1, type(r1)) # range(0, 0) <class 'range'>

d1 = {}
print(d1, type(d1)) # {} <class 'dict'>

# set {10}
s1 = {10}
print(s1, type(s1)) # {10} <class 'set'>

# bytes
b1 = bytes()
print(b1, type(b1)) # b'' <class 'bytes'>

# bytes array
b2 = bytearray()
print(b2, type(b2)) # bytearray(b'') <class 'bytearray'>

# frozenset 
f1 = frozenset()
print(f1, type(f1)) # frozenset() <class 'frozenset'>
