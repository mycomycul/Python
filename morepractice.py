# #Sample lambda function
# multi = lambda a,b : a*b
# print(multi(5,6))

# #Lambda in function
# def multiplier(n):
#     return lambda a:a*n

# mydoubler = multiplier(2)
# mytripler = multiplier(3)

# print(mydoubler(12))
# print(mytripler(12))


# #List as Array
# sauces = ["Salsa","Ketchup","Mayonnaise"]
# print(sauces[0])
# print(id(sauces))
# print(id(sauces[0]))
# sauces[0] = "Teriyaki"
# print(id(sauces))
# print(id(sauces[0]))


# #Looping Array
# for x in sauces:
#     print(x)

# sauces.pop(2)
# print(sauces)
# sauces.insert(2,"Mayonnaise")
# print(sauces)

# sauces.remove("Mayonnaise")
# print(sauces)
# sauces.append("Mayonnaise")
# sauces.sort()
# print(sauces)

#Dates
import datetime
def printinfo(x):
    print(x)
    print(x.year)
    print(x.strftime("%A"))

x = datetime.datetime.now()
printinfo(x)

x = datetime.datetime(2020,5,17)
printinfo(x)


