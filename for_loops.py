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


values = ["10 ", "20" , "30" , "0" , "-5" , "hello"]
def clean_positive_ints(values):
    clean_values=[]
    for i in values:
        try:
            j = int(i)
            if (j> 0):
                clean_values.append(j)      
        except ValueError:
            pass
    return clean_values   

    
result = clean_positive_ints(values)
print(result)




