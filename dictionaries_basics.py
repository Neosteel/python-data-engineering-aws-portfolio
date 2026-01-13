# person = { 
#     "name" : "Fatty",
#     "age" : 30,
#     "city" : "Brambleton"
# }

# print(person)
# print(type(person) )

# print(person.get("name"))
# print(person.get("age"))

# # adding a new value pair
# person["job"] = "target cashier"
# person["salary"] = 1500

# print(len(person))


# test = " hi hello"
# print(test.strip())

# # updating a existing key value 
# person["name"] = "Fatty"
# print(person)

# # aremove key
# person.pop("salary")
# print(person)


# # remove the last item
# person.popitem()
# print(person)

# # using del function 
# del person["city"]
# print(person)

# looping throught dictinaries 
employee = {
    "name" :"fatty",
    "salary" : 50000,
    "role" : "tester",
    "organization" : {
        "company": "c h robinson",
        "state" : "masacehttes",
        "type": "remote"
            },
 "married" : True
}

print(employee["organization"]["state"])
print(employee["organization"].keys())


#  loop syntnax for keys  
#  for key in dictname :
#     print(key)
# for key in employee:
#     print(key)

# # loop syntax for values 
# for value in employee.values():
#     print(value)


# #  to vchck if a key exists in dic 
# if "name" in employee:
#     print("Name exists")

#
# employee = {
#     "id": 101,
#     "profile": {
#         "name": "Neo",
#         "role": "QA Engineer"
#     }
# }

# print(employee["profile"]["role"])
