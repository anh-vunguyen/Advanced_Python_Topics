import json
from user import User
# Example
person = {"name": "John",
          "age": 30,
          "city": "New York",
          "hasChildren": False,
          "titles": ["engineer", "programmer"]
         }

# Serialization / Encoding
person_json = json.dumps(person, indent=4, sort_keys=True) # Dump to string
print(person_json)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Deserialization / Decoding
print("Decoding")
people = json.loads(person_json)
print(people)

with open('person.json', 'r') as file:
    new_person = json.load(file)
    print(new_person)

# Work with custom Class
user = User('Max', 27)
# Custom encoding function
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable.')

user_json = json.dumps(user, default=encode_user)
print(user_json)

# Custom JSON Encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(user, cls=UserEncoder)

user_json = UserEncoder().encode(user)
print(user_json)

# Custom JSON Decoder
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(user_json, object_hook=decode_user)
print(type(user))
print(f"Name: {user.name}, Age: {user.name}, Type: {user.__class__.__name__}")
