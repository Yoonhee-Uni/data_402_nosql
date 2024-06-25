import json

path_to_json = "starships_json.json"
with open(path_to_json) as json_file:
    starships = json.loads(json_file.read())
data= starships["results"])
# value = starships["count"]
# print(value)


# path_to_json = "example.json"
# with open(path_to_json) as jsonfile:
#     json_data = json.loads(jsonfile.read())
# value = json_data["ip"]
# print(value)
