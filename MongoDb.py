import pymongo
#Start Server
myclient = pymongo.MongoClient("127.0.0.1", 27017)
#Create Database
mydb = myclient["mydatabase"]
#Create Collection in Database
mycol = mydb["customers"]
 
#Create and insert a single entry
# mydict = {"name" : "John","address":"Highway 37"}
# x = mycol.insert_one(mydict)

#create and insert a list of entries
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

print(x.inserted_ids)

#Pull all database names into list and check if the specified database exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists")




