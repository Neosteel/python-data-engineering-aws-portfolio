import csv



# file open the csv file in "r'"" is read mode
file = open("raw_sales.csv", "r")  
# reader istores the csv with dicreader converting header coulms into keys and assingng rows for the ones below ....
reader = csv.DictReader(file)
# rows will create a list with the dictionaties as elemenrs 
rows = list(reader)  


print(type(rows))
# print(rows[0])
print(rows)


# for r in rows:
#     print(r)
# 'order_id': '1001', 'customer': 'Alice', 'product': 'Laptop', 'quantity': '1', 'price': '1200', 'email': 'alice@gmail.com'}
def clean_csv(rows):
    clean = [] 
    invalid = 0 

    for r in rows:
        order_id = r.get("order_id", "") 
        customer = r.get("customer", "")
        product = r.get("product", "")
        quantity_raw = r.get("quantity", "")
        email = r.get("email", "")
        price_raw = r.get("price",  "")


        if not email or not price_raw.isdigit() or not quantity_raw.isdigit():
            invalid +=1
            continue

        
        clean.append({
        # normalization after validation
    "order_id": int(order_id),
    "customer": customer,
    "product": product,
    "quantity": int(quantity_raw),
    "price": int(price_raw),
    "email": email
})

        
    return clean, invalid

cleaned_rows, invalid_count = clean_csv(rows)
print(cleaned_rows)
print("invalid:", invalid_count)



def create_cleaned_csv(clean_csv):
    with open("cleaned_rows.csv", "w" , newline="") as f :
        
        
        writer = csv.DictWriter(F, Fieldnames=["order_id", "customer", "product", "quantity", "price", "email"])
        extrasaction="ignore"
        writer.writeheader() 
        # Just the first row (column names).
        writer.writerows(cleaned_rows)
        # Write the rows


# When writing CSV from list of dictionaries, we always do 4 steps:

# Open file in write mode

# Create DictWriter with fieldnames

# writeheader()

# writerows(data)