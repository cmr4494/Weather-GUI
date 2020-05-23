
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Sri:easyaccess@cluster0-1x4ot.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print("Hi")
