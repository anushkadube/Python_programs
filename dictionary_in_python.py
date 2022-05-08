
print("To learn and understand dictionary in python")
mydictionary = { 'key1' : 'value1' , 'key2': 'value2' , 'key3': 'value3'}
print(mydictionary)

mydictionary = { 1: 'edureka' , 2: 'python' , 3: 'data science'}
print(mydictionary[1])
print(mydictionary.get(1))


mydictionary = { 1: 'edureka', 2: 'python' , 3: 'data science'}
print(mydictionary)
mydictionary[3] = 'artificial intelligence' #replacing an element in pyhton
print(mydictionary)

a = {1 : 2, 2 : 3, 3 : 4}
print("Empty dictionary: ",a.clear())
a = {1 : 2, 2 : 3, 3 : 4}
print("Created a copy of dictionary",a.copy())
a.update({4: 6})
print("Updated dictionary",a)


"""
There are various other operations on dictionary in python
clear()
copy()
values()
update()
fromkeys()
get()
items()
keys()
pop()
popitem()
setdefault()
"""
