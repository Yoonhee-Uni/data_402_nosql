import requests
import json
import pymongo

client = pymongo.MongoClient()
db = client.starwars
db.temp_test.drop()
db.create_collection("temp_test")


url = 'https://swapi.dev/api/starships'
response = requests.get(url)
sw_list_full = json.loads(response.text)
sw_list = response.json()['results']
# print(sw_list_full)

def starship_info(starship_name):

    pilot_names = []
    ship_check = False
    for ship_names in sw_list:
        if ship_names['name'] == starship_name:
            # print(f"Information on {starship_name}:")
            # print(ship_names['url'])
            # print(ship_names['model'])
            # print(ship_names['manufacturer'])
            # print(ship_names['length'])
            # print(ship_names['max_atmosphering_speed'])
            # print(ship_names['crew'])
            # print(ship_names['passengers'])
            # print(ship_names['pilots'])

            pilots_list = (ship_names['pilots'])
            ship_check = True
            print(pilots_list)
    if ship_check == False:
        return "No such ship."

    for pilot in pilots_list:
        pilot_url = pilot
        response_pilot = requests.get(pilot_url)
        pilot_names.append(response_pilot.json()['name'])

    # print(pilot_names)
    id_list = []
    for a_pilot in pilot_names:
        # print(db.characters.find_one({
        #     'name': a_pilot
        # },
        #     {'name': 1}))
        pilot_objid = db.characters.find_one({
            'name': a_pilot
        },
            {'name': 1})['_id']
        print(pilot_objid)
        id_list.append(pilot_objid)
    #print(id_list)
    return id_list

def add_starship(name):
    id_list = starship_info(name)
    if id_list == "No such ship.":
        return
    print(id_list)
    #db.temp_test.insert_one({'pilot': id_list})
    #what_was_added = db.temp_test.find_one({'pilot': id_list})
    #print(what_was_added)

    for ship in sw_list:
        if ship['name'] == name:
            # ship_name = ship['name']
            # ship_model = ship['model']
            # ship_manu = ship['manufacturer']
            # ship_len = ship['length']
            # ship_maspeed =
            # ship_crew
            # ship_pass
            db.temp_test.insert_one({
                'name': ship['name'],
                'model': ship['model'],
                'manufacturer': ship['manufacturer'],
                'length': ship['length'],
                'max_atmosphering_speed': ship['max_atmosphering_speed'],
                'crew': ship['crew'],
                'passengers': ship['passengers'],
                'pilot': id_list

            })