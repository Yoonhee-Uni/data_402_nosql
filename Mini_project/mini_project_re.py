import requests
import json
import pymongo

# 1. get startships data
# 2. extract all the data from starships
# 3.get pilots data
# 4. find matching name wit pilot data
# 5.and insert to starships in my db

def connect_server():
    client = pymongo.MongoClient()
    db = client["starwars"]
    return db

def starship(num : int):

    url = f'https://swapi.dev/api/starships/{num}/'
    response = requests.get(url)
    starships_list = response.json()

    if response.status_code == 200:
        name = starships_list['name'],
        model = starships_list['model'],
        manufacturer = starships_list['manufacturer'],
        length = starships_list['length'],
        max_atmosphering_speed = starships_list['max_atmosphering_speed'],
        crew = starships_list['crew'],
        passengers = starships_list['passengers'],
        pilots = starships_list['pilots']

        # return name, model, manufacturer, length, max_atmosphering_speed, crew, passengers, pilots
    else:
        return "no pilot"

    names = find_name(pilots)
    #find_name ['Luke Skywalker', 'Chewbacca', 'Han Solo']
    pilot_ids = find_id(names)

    # insert data(starship and pilot_id)
    db = connect_server()
    db.starships.insert_one({
        "name": name[0],
        "model": model[0],
        "manufacturer": manufacturer[0],
        "length": length[0],
        "max_atmosphering_speed": max_atmosphering_speed[0],
        "crew": crew[0],
        "passengers": passengers[0],
        "pilot": pilot_ids
    })


# print(starship(2))

def find_name(pilots):
    name_list=[]
    if len(pilots) == 0:
        return "No Pilot"
#get names
    else:
        for pilot in pilots:
            url = requests.get(pilot)
            url_in_json = url.json()
            name = url_in_json['name']
            name_list.append(name)
    return name_list

def find_id(names):
#connect db
    ids=[]
    db = connect_server()
    for i in names:
        id = db.characters.find({"name": f"{i}"}, {"_id" : 1})
        ids.append(id.next()['_id'])
    print(ids)
    return ids






# find_id()

print(starship(22))
# print(find_name(22))