import pymongo

def launch():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["my_database"]
    my_col = my_db["customers"]

    my_list = [
        {"_id": 1, "name": "John", "address": "Highway 37"},
        {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 3, "name": "Amy", "address": "Apple st 652"},
        {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
        {"_id": 5, "name": "Michael", "address": "Valley 345"},
        {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    ]

    x = my_col.insert_many(my_list)
    print(x.inserted_ids)