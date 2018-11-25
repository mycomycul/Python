import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {"name" : "John","address":"Highway 37"}

x = mycol.insert_one(mydict)
print(x.inserted_id)

# print(myclient.list_database_names())e
