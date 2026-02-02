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
# employee = {
#     "name" :"fatty",
#     "salary" : 50000,
#     "role" : "tester",
#     "organization" : {
#         "company": "c h robinson",
#         "state" : "masacehttes",
#         "type": "remote"
#             },
#  "married" : True
# }

# print(employee["organization"]["state"])
# print(employee["organization"].keys())

# print(employee["name"])
# employee["city"] = "new york"
# print(employee["city"])
# employee["vehicle"] = "car"
# print(employee)


# #  loop syntnax for keys  
# #  for key in dictname :
# #     print(key)
# # for key in employee:
# #     print(key)

# # # loop syntax for values 
# # for value in employee.values():
# #     print(value)


# # #  to vchck if a key exists in dic 
# # if "name" in employee:
# #     print("Name exists")

# #
# # employee = {
# #     "id": 101,
# #     "profile": {
# #         "name": "Neo",
# #         "role": "QA Engineer"
# #     }
# # }

# # print(employee["profile"]["role"])


# #  task 1 
# car = { 
#     "brand" : "toyota",
#     "year" : "2000",
#     "electric" : False
# }

# print(car)
# print(car["brand"])
# print(car.get("year"))

# # updating the key value pair by adding a new one 
# car["colour"] = "black"
# print(car)

# # updating the year to 2022 
# car["year"]= 2022
# print(car)


# # task 3 
# # deleting the key = electric
# del car["electric"]
# print(car)

# # task 4 looping through car
# for i in car:
#     print(i)

# # print values
# for j in car.values():
#     print(j)


# # looping thorogh key value pairs
# for k,v in car.items():
#     print(k,"=>",v)


# # check key exists
# if "price" in car:
#     print("price exists", car["price"])
# else:
#    print("price not available")



# counting pattern 
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# output = {} 
 
# for i in words:
#     if i in output:
#         output[i] += 1
#     else:
#         output[i] = 1 

# print(output)

# car["gears"] = 2
# print(car)

# test = {"a": 1, "b": 2}

# for k in test:
#     print(k, test[k])


# fruits = { 
#     "apple" : "red",
#     "guava" : "green",
#     "orange" : "orange",
#     "watermelon" : "green"
# }

# for  i in fruits:
#     print(i ,fruits[i])

logs = [
    {"status": 200, "endpoint": "/login"},
    {"status": 500, "endpoint": "/login"},
    {"status": 200, "endpoint": "/home"},
    {"status": 404, "endpoint": "/profile"},
    {"status": 200, "endpoint": "/login"},
    {"status": 500, "endpoint": "/profile"},
]

count_dict = {}
for i in logs:
    if i["status"] >= 400:
        count_dict[i["endpoint"]] = count_dict.get(i["endpoint"],0) + 1 
    else:
        pass
    

print(count_dict)