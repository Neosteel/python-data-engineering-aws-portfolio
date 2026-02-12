import requests
import csv
from datetime import datetime



URL =   "https://jsonplaceholder.typicode.com/users"
response = requests.get(URL)
response.raise_for_status()

users = response.json()

# print(type(users))
# # print(users[0])
# #  to avoid printing the full record everytime we can use the following 
# print(users[0].keys())

# Step 2: Extract clean data from API JSON

# 👉 Task:
# Create a function that returns only name + email from users.

# def extract_user_contacts(users):
#     contact = [] 
#     for u in users:
#         contact.append({"name":u.get("name", "UNKNOWN"),"email":u.get("email","UNKNOWN")})
    


#     return contact

# final = extract_user_contacts(users)
# print(final)

print(users[0])

def clean_users_from_api(users):
    contact_info = []
    invalid = 0 

    for u in users:
                address = u.get("address", {})
                name = u.get("name", "UNKNOWN")
                email = u.get("email", "")
                # validation row 
                if not email:
                    invalid +=1
                    continue

                

                # append to list 

                contact_info.append({
                                        "name": name,
                                        "email": email,
                                        "city": address.get("city", "UNKNOWN"),
                                        "website": u.get("website", "UNKNOWN")
                                    })
       

    return contact_info , invalid
clean_users , invalid = clean_users_from_api(users)




# creating a csv 
def export_to_csv(rows, filename):
    with open(filename,"w", newline="") as f :
        writer  = csv.DictWriter(f, fieldnames=["name", "email", "city","website"])
        writer.writeheader()
        writer.writerows(rows)


export_to_csv(clean_users, "users_clean.csv")
print("✅ CSV created: users_clean.csv")


# clean data with exampel




print("Run time:", datetime.now().isoformat())
print("Total input records:", len(users))
print("Clean records written:", len(clean_users))
print("Invalid records skipped:", invalid_count)


