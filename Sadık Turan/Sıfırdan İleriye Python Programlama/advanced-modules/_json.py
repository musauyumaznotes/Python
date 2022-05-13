import json


person_string = '{"name":"Ali","languages":["python","C#"]}'
# result = person["name"]
# result = person["languages"]
# result = person["languages"][1]

result =json.loads(person_string)
result = result["name"]
print(result)