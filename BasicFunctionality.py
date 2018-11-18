# #Class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def printMyName(self):
#         print("Hello my name is " + self.name)

# p1 = Person("Bobo", 36)
# p1.printMyName()
# #Delete
# del p1.age

# #Iterator
# mytuple = ("apple", "banana", "cherry")
# #Create Iterator Object
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# for x in mytuple:
#     print(x)

# #Create Iterable class
# class MyNumbers:
# #       create iterator to return
#     def __iter__(self):
#         self.a = 1
#         return self
# #       create next method 
#     def __next__(self):
#         #   Stoper iteration if more than 20 iterations
#         if self.a <= 20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
#         x=self.a
#         self.a += 1
#         return x
    
# myclass = MyNumbers()
# myiter = iter(myclass)

# for n in range(6):
#     print(next(myiter))
# print(next(myiter))

# for n in myiter:
#     print(n)


#Import Module
import mymodule #"import module_name as alias_name" for alias 

mymodule.greeting("Michael")
print("You are ",mymodule.person["age"], " years of age")

#Import Built-in Modules
import platform
x = platform.system()
print(x)

#List all function names contained in a module
print(dir(platform))

#Import portion of module
from mymodule import person
#portions imported are referred to by their portion name
print(person["country"])



#Working with JSON
import json

x = '{"name":"Michael","age":31,"city":"Seattle"}'
y = json.loads(x)

print(y["age"])
print(y)

z = {
    "name":"Michael",
    "age":31,
    "city":"Seattle"
    }

k = json.dumps(z)

print(k)

p = x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(p)
#Print json in indented formatting, sorted
print(json.dumps(p, indent=3, sort_keys=True))

