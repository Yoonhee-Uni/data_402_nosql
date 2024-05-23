import pymongo

#connecting to MongoDB
client = pymongo.MongoClient()
db = client["starwars"]

# db.collection.insert_one()
# db.collection.update_many()
# Retrieve a document from the database

luke = db.characters.find({"name": "Luke Skywalker"})
for character in luke:
    print(character)
#G etting only certain fields

# luke_short= db.characters.find_one({"name": "Luke Skywalker"}, {"name": 1, "eye_color": 1, "_id": 0})
# print(luke_short)
#
# #iterating through multiple recods/documents
# droids = db.characters.fine({"species.name": "Droid"})
# print(droids)
# for droid in droids:
#     print(droid["name"])

