# Python program to read
# json file


import json

# Opening JSON file
f = open('user.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# for key,value in data['user-instagram']:
#     print(key)
#     print(value)

id=data['user-instagram']['insta-id']
print(id)
# Closing file
f.close()
