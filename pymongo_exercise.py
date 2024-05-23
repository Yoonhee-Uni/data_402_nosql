import pymongo


# db.collection.insert_one()
# db.collection.update_many()

# Exercise 1 - Find the height of Darth Vader, only return results for the name and the height.
def connect_server():
    client = pymongo.MongoClient()
    db = client["starwars"]
    return db

def find_height():
    db = connect_server()
    luke = db.characters.find({"name": "Darth Vader"},{"_id":0 ,"name": 1, "height" : 1})
    for character in luke:
        print(character)

# Exercise 2 - Find all characters with yellow eyes, only return results for the names of the characters.
def find_yellow_eyes():
    db = connect_server()
    for document in db.characters.find({"eye_color": "yellow"}, {"_id": 0, "name": 1, "eye_color": 1}):
        print(document)

#Exercise 3 - Find male characters. Limit your results to only show the first 3.
def find_male():
    db = connect_server()
    for document in db.characters.find({"gender": "male"}, {"_id": 0}).limit(3):
        print(document)

#Exercise 4 -Find the names of all the humans whose homeworld is Alderaan.
def find_alderaan():
    db = connect_server()
    for document in db.characters.find({"homeworld.name": "Alderaan"}, {"_id": 0}):
        print(document)

find_alderaan()




