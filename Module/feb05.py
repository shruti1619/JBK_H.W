import json

#-----------------------python to json coversion using dumps() method----------------------------

# data={
#     "name": "John Doe",
#     "age": 30,
#     'is_student': False,
#     "city": "New York",
#     "hobbies": ["reading", "traveling", "coding"],
    
# }

# print(type(data))
# json_data=json.dumps(data, indent=4)
# print(type(json_data))
# print()
# print(data)
# print("----------------------------")
# print(json_data)

#------------------pyhton to json coversion using dump() method file handling----------------------------

data={
    "name": "John Doe",
    "age": 30,
    'is_student': False,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"],
    
}
with open('data.json','a') as file:
    json.dump(data,file,indent=4)
    
    

#-----------------------json to python coversion using load() method by file handling--------------------------------
with open('data.json','r') as file:
    data_loaded=json.load(file)
    print(type(data_loaded))
    print(data_loaded)

# -----------------------json to python coversion using loads() method--------------------------------

# json_string='''{
#     "name": "John Doe",
#     "age": 30,
#     "is_student": false,
#     "city": "New York",
#     "hobbies": [
#         "reading",
#         "traveling",
#         "coding"
#     ]
# }'''

# data=json.loads(json_string)
# print(type(json_string))
# print(type(data))
# print()
# print(json_string)
# print("----------------------------")   
# print(data)