student = {"name": "Hary", "age": 30, "address": "KTM"}

# update()
# get()

# keys
keys = student.keys()
print(keys) #dict_keys(['name', 'age', 'address'])
keys = list(keys) # to change the keys into list 

# values 
values = student.values()
print(values) # dict_values(['Hary', 30, 'KTM'])

#items
items = student.items()
print(items) #dict_items([('name', 'Hary'), ('age', 30), ('address', 'KTM')]) //returns in tuple

items = list[items]
print(items) # list[dict_items([('name', 'Hary'), ('age', 30), ('address', 'KTM')])]

a, b = items[0] # "name", "harry"
print(a) # tuple unpacking 
print(b)