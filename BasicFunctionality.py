#Claass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printMyName(self):
        print("Hello my name is " + self.name)

p1 = Person("Bobo", 36)
p1.printMyName()
#Delete
del p1.age

#Iterator
mytuple = ("apple", "banana", "cherry")
#Create Iterator Object
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)

#Create Iterable class
class MyNumbers:
#       create iterator to return
    def __iter__(self):
        self.a = 1
        return self
#       create next method 
    def __next__(self):
        #   Stoper iteration if more than 20 iterations
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        x=self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

for n in range(6):
    print(next(myiter))
print(next(myiter))

for n in myiter:
    print(n)




