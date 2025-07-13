# python data dict
import json
pythonData = {
  "username": "renuka27",
  "email": "renuka@example.com",
  "skills": ["Python", "Git", "VSCode"],
  "active": True
}

# convert dic to json
convertedData = json.dumps(pythonData)
print(type(convertedData))
print(convertedData)

# write to profile.json
with open('profile.json', 'w') as p:
    json.dump(pythonData, p)

# read from profile.json
with open('profile.json', 'r') as p:
    data = json.load(p)
    print("read from file", data)
    # back = json.loads(data)
    print('skills', data["skills"])



