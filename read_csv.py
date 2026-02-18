import csv



# # file open the csv file in "r'"" is read mode
# file = open("raw_sales.csv", "r")  
# # reader istores the csv with dicreader converting header coulms into keys and assingng rows for the ones below ....
# reader = csv.DictReader(file)
# # rows will create a list with the dictionaties as elemenrs 
# rows = list(reader)  


# print(type(rows))
# # print(rows[0])
# print(rows)


# # for r in rows:
# #     print(r)
# # 'order_id': '1001', 'customer': 'Alice', 'product': 'Laptop', 'quantity': '1', 'price': '1200', 'email': 'alice@gmail.com'}
# def clean_csv(rows):
#     clean = [] 
#     invalid = 0 

#     for r in rows:
#         order_id = r.get("order_id", "") 
#         customer = r.get("customer", "")
#         product = r.get("product", "")
#         quantity_raw = r.get("quantity", "")
#         email = r.get("email", "")
#         price_raw = r.get("price",  "")


#         if not email or not price_raw.isdigit() or not quantity_raw.isdigit():
#             invalid +=1
#             continue

        
#         clean.append({
#         # normalization after validation
#     "order_id": int(order_id),
#     "customer": customer,
#     "product": product,
#     "quantity": int(quantity_raw),
#     "price": int(price_raw),
#     "email": email
# })

        
#     return clean, invalid

# cleaned_rows, invalid_count = clean_csv(rows)
# print(cleaned_rows)
# print("invalid:", invalid_count)



# def create_cleaned_csv(clean_csv):
#     with open("cleaned_rows.csv", "w" , newline="") as f :
        
        
#         writer = csv.DictWriter(f, fieldnames=["order_id", "customer", "product", "quantity", "price", "email"], 
#         extrasaction = "ignore")
    
#         writer.writeheader() 
#         # Just the first row (column names).
#         writer.writerows(cleaned_rows)
#         # Write the rows
        
# create_cleaned_csv(cleaned_rows)

# cleaned_rows, invalid_count = clean_csv(rows)

# print(cleaned_rows)
# print("invalid:", invalid_count)

# create_cleaned_csv(cleaned_rows)
# print("✅ cleaned_rows.csv created")


# When writing CSV from list of dictionaries, we always do 4 steps:

# Open file in write mode

# Create DictWriter with fieldnames

# writeheader()

# writerows(data)

# cleaned_rows, invalid_count = clean_csv(rows)





# print(cleaned_rows)
# print("invalid:", invalid_count)
# # cleaned_rows.csv is created in the pyton journey folder now 
# create_cleaned_csv(cleaned_rows)
# print("✅ cleaned_rows.csv created")






#  now read the cleaned_rows.csv 

# # def read_cleaned_rows():
with open("cleaned_rows.csv" , "r") as f :
    reader = csv.DictReader(f)
    cleandata = list(reader)


revenue_per_product = {}

for r in cleandata:
        # {'order_id': 1001, 'customer': 'Alice', 'product': 'Laptop', 'quantity': 1, 'price': 1200, 'email': 'alice@gmail.com'},
    product = r["product"]
    quantity = (int(r["quantity"]))
    price = (int(r["price"]))

    revenue = price * quantity

    if product not in revenue_per_product:
        revenue_per_product[product] = 0 

        revenue_per_product[product] += revenue

print("revenue_per_product : ")
for  product , total in revenue_per_product.items():
    print(product , total)

# if key not in dictionary:
#     dictionary[key] = initial_value

# dictionary[key] += something


sorted(revenue_per_product.items() , key = lambda x : x[1])

# lets put the sortd values into a variable 
sorted_values = sorted(revenue_per_product.items() , key = lambda x : x[1])

n = int(input("enter a number : "))
top_n = n 
top_product = sorted_values[:n]

if n <= len(sorted_values):
    for product , total in top_product:
        print(product , total)


print(cleandata)



# revenue per product : 

# Business Question: {'order_id': '1001', 'customer': 'Alice', 'product': 'Laptop', 'quantity': '1', 'price': '1200', 'email': 'alice@gmail.com'}

# “Give me total revenue per customer.”

# What You Must Think:

# Revenue = price × quantity

# Group by customer

# Add revenue for each customer

    # cleandata  is the list we got with cleaned data from our raw csv 
# {'order_id': '1001', 'customer': 'Alice', 'product': 'Laptop', 'quantity': '1', 'price': '1200', 'email': 'alice@gmail.com'}
# revenue_per_customer = {} 

# for r in cleandata:
#     customer = r.get("customer","")
#     revenue= int(r["price"]) * int(r["quantity"])
    
#     if customer not in revenue_per_customer: 
#         revenue_per_customer[customer] = 0
#     revenue_per_customer[customer] = revenue_per_customer.get(customer, 0) + revenue
# top_2 = 0 

# sorted_reveune = sorted(revenue_per_customer.items() , key = lambda x : x[1], reverse = True)

# top_2 = sorted_reveune[:2]
# for i in top_2:
#     print(i)



#  lets no calculate revenue of customr per product 

revenue_by_customer_product = {}

for l in cleandata:
    customer = l.get("customer","")
    product = l.get("product","")
    price = int(l.get("price",""))
    quantity = int(l.get("quantity",""))
    revenue = price * quantity

    key = (customer , product) 

    if key not in revenue_by_customer_product:
        revenue_by_customer_product[key] = 0 

    revenue_by_customer_product[key] =+ revenue

for key ,revenue in revenue_by_customer_product.items():
    print(key,revenue)