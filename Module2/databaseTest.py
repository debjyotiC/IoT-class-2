import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_connect = myclient["test_DB"]  # database name
db_collection = db_connect["sensor_data"]

query = {"api_key": "KDT6QF1NGR35KXKL0Q-DOG"}

reply_got = [i for i in db_collection.find(query)][0]
reply = {"data": reply_got["field1"], "date": reply_got["date"]}
print(reply)
