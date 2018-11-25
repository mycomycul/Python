import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# #Find One and print
# print(mycol.find_one())

# #Find All and Print. Equal to SELECT *
# for x in mycol.find():
#     print(x)

#Use second find parameters to only return some fields.
#0 for blacklist, 1 whitelist. All obejcts must be the same 0 or 1 except _id 

# #Blacklist - Show only fields not specified 0
# for c in mycol.find({},{"_id":0,"name":0}):
#     print(c)

# #Whitelist - Show only field specified with 1
# for c in mycol.find({},{"_id":0,"name":1}):
#     print(c)


##Filtering##
#Create Query where address = "Yellow Garden 2"
myquery = {"address":"Yellow Garden 2"}
mydoc = mycol.find(myquery,{"_id":0})

for b in mydoc:
    print(b)
#Create query where id = 1
myquery = {"_id":1}
mydoc = mycol.find(myquery,{"_id":1,"name":1})

for b in mydoc:
    print(b)

##Advanced Query##
#Filter where address starts with value less than ($lt) "S"
myquery = {"address":{"$lt":"S"}}
mydoc = mycol.find(myquery)

for b in mydoc:
    print(b)

#Regular Expressions
myquery = {"name":{"$regex":"^S"}}
mydoc = mycol.find(myquery)

for b in mydoc:
    print(b)

##Sorting##
#sort() takes one parameter for fieldname and one optional for direction
mydoc = mycol.find({},{"_id":0}).sort("name")
for b in mydoc:
    print(b)

#Sort Descending
mydoc = mycol.find({},{"_id":0}).sort("name",-1)
for b in mydoc:
    print(b)

##Delete Document##
myquery = {"address":"Park Lane 38"}

#Deletes first matching document
mycol.delete_one(myquery)

#Deletes all matching documents
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted")

#Delete all documents
x = mycol.delete_many({})
print(x.deleted_count, " document deleted")

#Delete Collection



collectionlist = mydb.list_collection_names()
print(collectionlist)
print(mycol.drop())
collectionlist = mydb.list_collection_names()
print(collectionlist)

