import json 

data=json.load(open("data.json", "r"))
data["UserID"].append(input())
json.dump(data, open("data.json", "w"))