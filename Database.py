import pymongo

class Database:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["database"]
        self.collection = database["WeatherInfo"]

    def insert(self, temp_F, temp_C, cloud, date, time):
        toInsert = {"temp_F": temp_F, "temp_C": temp_C, "cloud conditions": cloud, "date": date, "time": time}
        self.collection.insert_one(toInsert)
if __name__ == "__main__":
    database = Database()
    database.insert(420, 69, "shadyaf", "4/20/69", "4:20:69")




