# dict 
# Uising dict we can store key value pairs
# In dict key can be either string or integer

# methods:
# 'clear', 
# 'copy', 
# 'items', 
# 'keys', 
# 'pop', 
# 'update', 
# 'values'
# d1={}
# print(d1,type(d1)) # {} <class 'dict'>

d1 = {1 : 10, 2 : 10, 3 : 10, 4 : 10}
# print(d1) # {1: 10, 2: 10, 3: 10, 4: 10}
# print(d1.get(1)) # 10
# print(d1.keys()) # dict_keys([1, 2, 3, 4])
# print(d1.values()) # dict_values([10, 10, 10, 10])
# print(d1.items()) # dict_items([(1, 10), (2, 10), (3, 10), (4, 10)])
# d1.update({11:22})
# print(d1) # {1: 10, 2: 10, 3: 10, 4: 10, 11: 22}
d1 = {"nameone" : "Sai Kiran", "nametwo" : "Sai Ram"}
d1["nametwo"] = "Sai Kumar"
print(d1)  # {'nameone': 'Sai Kiran', 'nametwo': 'Sai Kumar'}

d1 = {1: 10, 2: 20, 3: 30, 4 : 40}
d2 = {"nameone" : "Sai Kiran", "nametwo": "Sai Ram"}
d1.update(d2)
print(d1)  # {1: 10, 2: 20, 3: 30, 4: 40, 'nameone': 'Sai Kiran', 'nametwo': 'Sai Ram'}

d1 = {1: 10, 2: 20, 3: 30, 4 : 40}
d1.update({1: "NameOne"})
print(d1)  # {1: 'NameOne', 2: 20, 3: 30, 4: 40}

d1 = {1: 10, 2:20, 3:30, 4: 40, 5: 50}
d1["NameOne"] = d1.pop(1)
print(d1)  # {2: 20, 3: 30, 4: 40, 5: 50, 'NameOne': 10}
