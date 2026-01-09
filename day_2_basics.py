# name = "naveen"
# years_of_experience = 5 
# learning_path = "Python + data engineering + aws "

# print(name)
# print(years_of_experience)
# print(learning_path)


# x = 10
# y  = 11 

# print(x+x)
# print(y+y)

# a = 10
# b = "10"

# print(a + a)
# print(b + b)

# a = 10
# b = "10"
# c = 10.5

# print(type(a))
# print(type(b))
# print(type(c))


# age_str = "25"
# age_int = int(age_str)

# height_str = "5.8"
# height_float = float(height_str)

# print(age_int + 5)
# print(height_float + 1.2)
# print(type(age_int))
# print(type(height_float))


# user input : 

# name = input("enter your name  ")
# age = input(" enter your age")


# print(type(name))
# print(type(age))

# practise problems uintil variables topic 

# # # 1)take two unputs from a user 
# # name = input("enter name")
# # balance = int(input("enter the account balance"))

# # print(type(name))
# # print(type(balance))


# # print(float(name))
# # print(float(balance))

# # problem 1 
# # user enter value 
# value1 = input("enter the first value  :")
# value2 = input("enter the secpnd value  :")
# # printing the entered values 
# print(value1)
# print(value2)
# # type of the values 
# print(type(value1))
# print(type(value2))

# value1_float = float(value1)
# value2_float = float(value2)

# print(value1_float)
# print(value2_float) 


# print(type(value1_float))
# print(type(value2_float))

# task 3 
# a = int(input("enter a value"))
# b = int(input("enter a value "))

# result = int(a) + int(b)
# print(result)
# print(type(result))

# # problem 3 
# record_count  = input("enter the record count: ")
# file_size_mb = input("enter the file size: ") 
# #  printing values
# print(record_count)
# print(file_size_mb)
# #  convert values 
# record_count_int = int(record_count)
# file_size_mb_float = float(file_size_mb)
# # print the converted values 
# print(record_count_int)
# print(file_size_mb_float)
# print(type(record_count_int))
# print(type(file_size_mb_float))

# record_count_raw = input("enter record count")
# try:
#     record_count= int(record_count_raw)
#     if(record_count  < 0 ):
#         print("INVALID: Negative count")
#     elif (record_count == 0):
#         print("STOP : NO DATA")
#     else(record_count > 0 ):
#         print("PROCEED : Records present")
# except:
#     print("INVALID: Non-numeric input")

# prolem : silent bug prevention 
# value_raw = input("enter the value: ")

# print(value_raw)
# print(type(value_raw))
# try:
#     value = int(value_raw)
#     print(value)
#     print(type(value))
# except:
#     print("INVALID INPUT")

# problem 3 : pipeline health check 
# record_count_raw = input("enter the record count: ")
# error_count_raw = input("enter the error count: ")
# try:
#     record_count=int(record_count_raw)
#     error_count= int(error_count_raw)
#     if(record_count == 0):
#         print("FAIL :No data")
#     elif(error_count > 0 ):
#         print("FAIL: Errors detected")
#     else:
#         print("SUCCESS: Pipeline clean")
# except:
#     print("INVALID INPUT")

# Functions : problem 1 
# def convert_to_int(value_raw):
#     try:
#         value=int(value_raw)
#         return value
#     except:
#         return None




# value_raw = input("enter a value : ")
# result = convert_to_int(value_raw)
# print(result)
# print(type(result))

# problem 2 : 
# def pipeline_status(record_count_raw,error_count_raw):
#     try:
#         record_count=int(record_count_raw)
#         error_count=int(error_count_raw)
#         if(record_count == 0):
#             return "FAIL: No data"
#         elif(error_count > 0):
#             return "FAIL: Errors detected"
#         else:
#             return "SUCCESS: Pipeline clean"
#     except:
#         return "INVALID INPUT"




# record_count_raw = input("enter a record count : ")
# error_count_raw = input("enter the error count : ")
# result = pipeline_status(record_count_raw,error_count_raw)
# print(result)


#  problem for functions :
# def to_int_or_none(raw):
#     try: 
#         value =raw.strip()
#         value_clean = int(value)
#         return value_clean
#     except:
#         return None

# def pipeline_status_v2(record_count_raw, error_count_raw):
#     record_count = to_int_or_none(record_count_raw)
#     error_count = to_int_or_none(error_count_raw)
#     try:
#         if(record_count == None or error_count == None):
#             return "INVALID INPUT"
#         elif(record_count < 0 or error_count < 0 ):
#             return "INVALID INPUT"
#         elif(record_count == 0):
#             return "FAIL: No data"
#         elif(error_count > 0):
#              return "FAIL: Errors detected"
#         else:
#             return "SUCCESS: Pipeline clean"
#     except: 
#         return "error in logic"




# record_count_raw = input("enter the record count : ")
# error_count_raw = input("enter the error count : ")

        
# print(pipeline_status_v2(record_count_raw, error_count_raw))


# ? problem 2 : tough 

def to_int_or_none(raw):
    try: 
        value =raw.strip()
        value_clean = int(value)
        return value_clean
    except:
        return None

def evaluate_run(record_count_raw, error_count_raw, max_error_allowed_raw):
    record_count = to_int_or_none(record_count_raw)
    error_count = to_int_or_none(error_count_raw)
    max_error_allowed = to_int_or_none(max_error_allowed_raw)
    if record_count is None or error_count is None or max_error_allowed is None:
        return "INVALID INPUT"
    elif(record_count < 0 or error_count < 0):
        return "INVALID INPUT"
    elif(record_count == 0 ):
        return "FAIL: No data"
    elif(error_count > max_error_allowed):
        return "FAIL: Too many errors"
    else:
        return "SUCCESS: Within error threshold"

    
    

record_count_raw = input("enter the record count: ")

error_count_raw = input("enter the error_count: ")

max_error_allowed_raw = input(" the max errors that can be allowed: ")

print(evaluate_run(record_count_raw, error_count_raw, max_error_allowed_raw))