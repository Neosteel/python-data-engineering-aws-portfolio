#  for loops used to repetitive taaks like printing or etc 
# 
# for value in [10,20,30]:
#     print(value)


# syntex : 
# for item in collection:
    # code block


# problem1: 
# values = ["10", "20", "30"]
# for i in values:
#     print(i)
#     print(type(i))


# problem 2 
# values = ["10", "0", "-5", "25"]
# for i in values:
#     j = int(i)
#     if (j > 0):
#         print(j)

# problem 3 Requirements

# 1️⃣ Loop through the list
# 2️⃣ Safely convert each value to int
# 3️⃣ If conversion fails → skip it
# 4️⃣ Print only integers greater than 0
# 5️⃣ Program must never crash

# ❗Rules

# Use for

# Use try/except

# No functions

# No helper utilities
# values = ["10", "abc", "0", "-5", "25"]

# for i in values:
#     try:
#         j = int(i)
#         if (type(j) == int and j>0):
#             print(j)
#     except:
#         print("skip it")

# append function 
#  syntax : my_list.append(value)
#  this will  add element to the list 

# example
# numbers = []
# numbers.append(10)
# numbers.append(20)
# numbers.append(30)

# print(numbers)

#  D NOT USE : numbers = numbers.append(10)
#  ITS WRONG 


# 🧪 PROBLEM 4 — Batch Cleaning with append() 


# values = ["10", "abc", "0", "-5", "25"]


# # Requirements

# # 1️⃣ Create an empty list called clean_values
# # 2️⃣ Loop through values
# # 3️⃣ Safely convert each value to int
# # 4️⃣ If conversion fails → skip
# # 5️⃣ If value is greater than 0 → add to clean_values
# # 6️⃣ After the loop → print clean_values once
        
        
# clean_values = []
# for i in values:
    
#     try:
#         j = int(i)
#         if (j> 0):
#             clean_values.append(j)
#     except:
#         pass
# print(clean_values)
        
# refactoring the problem into function s 

# the  concept of this proble was : raw list  →  function  →  clean list
# and make it into : raw list  →  clean_positive_ints(values)  →  clean list


# values = ["10 ", "20" , "30" , "0" , "-5" , "hello"]
# def clean_positive_ints(values):
#     clean_values=[]
#     for i in values:
#         try:
#             j = int(i)
#             if (j> 0):
#                 clean_values.append(j)      
#         except ValueError:
#             pass
#     return clean_values   

    
# result = clean_positive_ints(values)
# print(result)




# values = ["10 ", "20" , "30" , "0" , "-5" , "hello"]

# clean_values=[]
# for i in values:
#     try:
#         j = int(i)
#         if (j <=0):
#             continue
#         clean_values.append(j)      
#     except ValueError:
#             pass
 

    
# result = clean_values
# print(result)


# problem 1 : 
# 1️⃣ Loop through the list
# 2️⃣ Safely convert values to int
# 3️⃣ Skip invalid values (use continue)
# 4️⃣ Skip values ≤ 0
# 5️⃣ Collect valid values into a list
# 6️⃣ Return the list (do NOT print inside the function)

# raw_counts = ["10", " 5", "0", "-3", "abc", "20"]


# def validate_counts(raw_counts):
#     v_count = []
#     for i in raw_counts:
#         try:
#             j=int(i)
#             if(j<=0):
#                 continue
#             v_count.append(j)
#         except ValueError:
#             pass    
#     return v_count

# valid_count = print(validate_counts(raw_counts))

# 🔓 PROBLEM 2 — Threshold-Based Pipeline Decision

record_counts = ["100", "200", "abc", "-5"]
error_counts  = ["0", "3", "xyz"]

max_errors = 2 

def pipeline_decision(record_counts, error_counts, max_errors):
    valid_record_counts = []
    valid_error_counts = []

    for i in record_counts:
        try:
            j = int(i.strip())
        except ValueError:
            continue
        if j > 0:
            valid_record_counts.append(j)
    for k in error_counts:
        try:
            l = int(k.strip())
        except ValueError:
            continue
        if l > 0:
            valid_error_counts.append(l)
    if len(valid_record_counts) == 0 :
        return ("FAIL: NO DATA")
    
    for l in valid_error_counts:
        if l >max_errors:
            return "FAIL : TOO MANY ERRORS"

    return "SUCCESS"



result = pipeline_decision(record_counts, error_counts, max_errors)
print(result)



