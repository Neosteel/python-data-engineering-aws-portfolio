# # # person = { 
# # #     "name" : "Fatty",
# # #     "age" : 30,
# # #     "city" : "Brambleton"
# # # }

# # # print(person)
# # # print(type(person) )

# # # print(person.get("name"))
# # # print(person.get("age"))

# # # # adding a new value pair
# # # person["job"] = "target cashier"
# # # person["salary"] = 1500

# # # print(len(person))


# # # test = " hi hello"
# # # print(test.strip())

# # # # updating a existing key value 
# # # person["name"] = "Fatty"
# # # print(person)

# # # # aremove key
# # # person.pop("salary")
# # # print(person)


# # # # remove the last item
# # # person.popitem()
# # # print(person)

# # # # using del function 
# # # del person["city"]
# # # print(person)

# # # looping throught dictinaries 
# # # employee = {
# # #     "name" :"fatty",
# # #     "salary" : 50000,
# # #     "role" : "tester",
# # #     "organization" : {
# # #         "company": "c h robinson",
# # #         "state" : "masacehttes",
# # #         "type": "remote"
# # #             },
# # #  "married" : True
# # # }

# # # print(employee["organization"]["state"])
# # # print(employee["organization"].keys())

# # # print(employee["name"])
# # # employee["city"] = "new york"
# # # print(employee["city"])
# # # employee["vehicle"] = "car"
# # # print(employee)


# # # #  loop syntnax for keys  
# # # #  for key in dictname :
# # # #     print(key)
# # # # for key in employee:
# # # #     print(key)

# # # # # loop syntax for values 
# # # # for value in employee.values():
# # # #     print(value)


# # # # #  to vchck if a key exists in dic 
# # # # if "name" in employee:
# # # #     print("Name exists")

# # # #
# # # # employee = {
# # # #     "id": 101,
# # # #     "profile": {
# # # #         "name": "Neo",
# # # #         "role": "QA Engineer"
# # # #     }
# # # # }

# # # # print(employee["profile"]["role"])


# # # #  task 1 
# # # car = { 
# # #     "brand" : "toyota",
# # #     "year" : "2000",
# # #     "electric" : False
# # # }

# # # print(car)
# # # print(car["brand"])
# # # print(car.get("year"))

# # # # updating the key value pair by adding a new one 
# # # car["colour"] = "black"
# # # print(car)

# # # # updating the year to 2022 
# # # car["year"]= 2022
# # # print(car)


# # # # task 3 
# # # # deleting the key = electric
# # # del car["electric"]
# # # print(car)

# # # # task 4 looping through car
# # # for i in car:
# # #     print(i)

# # # # print values
# # # for j in car.values():
# # #     print(j)


# # # # looping thorogh key value pairs
# # # for k,v in car.items():
# # #     print(k,"=>",v)


# # # # check key exists
# # # if "price" in car:
# # #     print("price exists", car["price"])
# # # else:
# # #    print("price not available")



# # # counting pattern 
# # # words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# # # output = {} 
 
# # # for i in words:
# # #     if i in output:
# # #         output[i] += 1
# # #     else:
# # #         output[i] = 1 

# # # print(output)

# # # car["gears"] = 2
# # # print(car)

# # # test = {"a": 1, "b": 2}

# # # for k in test:
# # #     print(k, test[k])


# # # fruits = { 
# # #     "apple" : "red",
# # #     "guava" : "green",
# # #     "orange" : "orange",
# # #     "watermelon" : "green"
# # # }

# # # for  i in fruits:
# # #     print(i ,fruits[i])

# # logs = [
# #     {"status": 200, "endpoint": "/login"},
# #     {"status": 500, "endpoint": "/login"},
# #     {"status": 200, "endpoint": "/home"},
# #     {"status": 404, "endpoint": "/profile"},
# #     {"status": 200, "endpoint": "/login"},
# #     {"status": 500, "endpoint": "/profile"},
# # ]

# # count_dict = {}
# # for i in logs:
# #     if i["status"] >= 400:
# #         count_dict[i["endpoint"]] = count_dict.get(i["endpoint"],0) + 1 
# #     else:
# #         pass
    

# # print(count_dict)

# # probLem to solve :
# # Scenario (real-world):
# # You receive a batch of pipeline IDs from an upstream system. Some are dirty.
# # <!-- <!-- raw_batch_ids = ["101", " 202", "abc", "303", "", None, "404x", "505"] -->

# # raw_batch_ids = ["101","202","abc", "303","", None ,"404x","505"]


# # def clean_batch_ids(raw_batch_ids): 
# #     clean_id = []
# #     for i in raw_batch_ids:
# #         try:
# #             if i is None:
# #                 continue

# #             j = int(i.strip())
# #             clean_id.append(j)
# #         except:
# #             continue
# #     return clean_id

# # clean = clean_batch_ids(raw_batch_ids)
# # print(clean)



# #  problem 2 : 
# # A valid count is a positive integer only
# # (so 1200, 50, 800, "900" are valid after cleaning; -10, 0, None are invalid)

# # Classification:

# # >= 1000 → "HEALTHY"

# # 100–999 → "WARNING"

# # < 100 → "CRITICAL"

# # raw_record_counts =  [1200, 50, -10, 0, 800, "900", None]

# # def classify_pipeline_Health(raw_record_counts):

# #     valid_counts = []
# #     statuses = []
# #     for i in raw_record_counts:
# #         try:
# #             if (i is None):
# #                 continue
# #             j = int(i)
# #             if (j <=0):
# #                 continue

# #             valid_counts.append(j)

# #             if (j>= 1000):
# #                 statuses.append("HEALTHY")
# #             elif(j>=100 and j <= 999):
# #                 statuses.append("WARNING")
# #             elif(j< 100):
# #                 statuses.append("CRITICAL")
# #         except:
# #             continue
    
# #     return valid_counts, statuses

# # output = classify_pipeline_Health(raw_record_counts)
# # print(output)


# #  problem 3 : 
# # pipeline_names = ["orders", "users", "payments", "inventory"]
# # pipeline_status = ["SUCCESS", "FAILED", "FAILED", "SUCCESS"]
# # pipeline_latency_ms = [120, 4500, 8000, 200]


# # def find_failed_pipelines(pipeline_names, pipeline_status, pipeline_latency_ms):
# #     failed = []
# #     try: 
# #         for i in range(len(pipeline_names)):
# #             if pipeline_status[i] == "FAILED" or pipeline_latency_ms[i] >5000:
# #                 failed.append(pipeline_names[i])
# #     except:
# #         pass
        
    
    
# #     return failed

# # failed_pipelines = print(find_failed_pipelines(pipeline_names, pipeline_status, pipeline_latency_ms))

# # Problem 1: Factorial (Iterative)

# # Write a function that returns the factorial of a number.

# # Input: 5

# # Output: 120

# # Do not use recursion.

# # num = int(input("Enter a number : "))

# # def fac(num):
# #     j = 1 
# #     while num>=1:
# #         j = j * num
# #         num -=1

# #     return j
# # factorial_of_number = (fac(num))


# # print(factorial_of_number)


        
# # Palindrome Check

# # Question:
# # Write a function that checks whether a string is a palindrome.

# # Rules

# # Ignore case

# # Return True or False

# # Use a function

# # No external libraries

# # word = input("enter a word to check : ")

# # def palindrome_check(word):
# #     # word = word.lower()
# #     # return word == word[::-1]
# #     reverse_word = ""
# #     for i in range(len(word)-1 , -1 , -1 ):
# #         reverse_word = reverse_word + word[i]
# #     if reverse_word == word:
# #         return True
# #     else:
# #         return False
        
# # number_is_palindrome =  print(f"the word is palidrom or not  : {palindrome_check(word)} ")

# # word = input("enter a word to check : ")

# # def first_non_repeating_char(word):
# #     for i in range(len(word)):
# #         count = 0   
# #         for j in range(len(word)):
# #             if word[j] == word[i]:
# #                 count = count + 1 
# #             if count == 1:
# #                 return word[i]
# #     return None

# # excellent_work = print(first_non_repeating_char(word))

# # num = int(input("enter a number : "))

# # def reverse_a_number(num):
# #     reverse = 0 

# #     while num > 0:
# #         digit = num%10
# #         reverse = reverse*10  + digit

# #         num = num //10
       
# #     return reverse

# # output = print(reverse_a_number(num))



# # num = int(input("enter a number : "))

# # def sum_of_number(num):
# #     sum = 0 

# #     while num > 0:
# #         digit = num%10
# #         sum = sum + digit

# #         num = num //10
       
# #     return sum

# # output = print(sum_of_number(num))


# # prime number
# # num = int(input("enter a number "))
# # n = 1

# # def prime_or_not(num):
# #     if num <=1:
# #         return False
    
# #     for i in range(2,num):
# #         if num%i == 0:
# #             return False
# #     return True

# # output = (f"the number is prime {prime_or_not(num)}")
# # print(output)

# # start patern 

# # n = int(input("enter a number"))

# # def star_pattern(n):
# #     j = "*"
# #     for i in range(1,n+1):
# #         print(j*i)
# # star_pattern(n)
        

# # pyramid_rows= int(input("enter a number"))

# # def num_pattern(pyramid_rows):
# #     for i in range(1,pyramid_rows+1):
# #         for j in range(1,i+1):
# #             print(j,end="")
# #         print()

# # output = num_pattern(pyramid_rows)

# # problem : arsmstrong number 

# # num = int(input("ENTER A NUMBER  : "))

# # def armstrong_number(num):
# #     armnum= 0
# #     original = num 

# #     while num >0:
# #         j = num%10 
# #         armnum = armnum + (j**(len(str(original)))) 
# #         num = num//10
        
# #     return armnum == original


# # output = armstrong_number(num)
# # print(output)

        

# # dic study 

# user = {"id": 101, "email": "a@b.com"}
# print(user["email"])

# print(user["id"])
# user["role"] = "admin"

# user["id"] = 102
# print(user)


# del user["role"]
# print(user)

# print(user.get("id"))

# # looping
# for k in user:
#     print(k)

# for i  in user.values():
#     print(i)

# # need boy key and balues 
# for k, v in user.items():
#     print(k, v)

# #  nested dic ( list in dict )
# data = {
#   "pipelines": [
#     {"name": "orders", "status": "SUCCESS"},
#     {"name": "users", "status": "FAILED"}
#   ]
# }
# print(data["pipelines"][1]["name"])   # "users"


# 
pipelines = [
    {"name": "orders", "status": "SUCCESS", "latency_ms": 120},
    {"name": "users", "status": "FAILED", "latency_ms": 4500},
    {"name": "payments", "status": "FAILED", "latency_ms": 8000},
    {"name": "inventory", "status": "SUCCESS", "latency_ms": 200}
]

# busiess problem: find all the failed pipelines or have latency <5000

def failed_pipelines(pipelines):
    success_pipeline = []
    for i in pipelines:
            if (i.get("status") == "FAILED" or i.get("latency_ms") > 5000):
                success_pipeline.append((i["name"]))
    return success_pipeline

output = failed_pipelines(pipelines)

print(output)

