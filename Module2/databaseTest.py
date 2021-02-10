import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")  # connect with DB
db_connect = db_client["test_DB"]  # database name
db_collection = db_connect["sensor_data"]  # collection name

query = {"api_key": "KDT6QF1NGR35KXKL0Q-DOG"}

reply_got = [i for i in db_collection.find(query)][-1]
reply = {"data": reply_got['field1'], "date": reply_got['date']}
print(reply)


