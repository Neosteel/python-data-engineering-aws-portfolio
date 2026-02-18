import csv 
from datetime import datetime
from datetime import datetime, timedelta


# sales_Data = []

# with open("sales_with_data.csv", "r" , encoding = "utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         sales_Data.append(row)
    
# print("Loaded data")
# for row in sales_Data:
#     print(row)

# print("\nParsing datetime data")
# for row in sales_Data:
#     date_str = row["date"]  # <-- important: take date from the CURRENT row
#     dt = datetime.strptime(date_str, "%Y-%m-%d")
#     print(date_str, "->", dt, "|", dt.year, dt.month, dt.day)


# # provide revenue per month 

# revenue_per_month = {}

# for r in sales_Data:
#     dt = datetime.strptime(row["date"], "%Y-%m-%d")
#     # creating mopnth key 
#     month_key = f"{dt.year}-{dt.month:02d}"
#     revenue = int(row["price"]) * int(row["quantity"])

#     revenue_per_month[month_key] = revenue_per_month.get(month_key, 0) + revenue
    # Accumulate Revenue Per Month
    # Group by month + Sum revenue




# compare two dates "2026-03-01" and "2026-02-15"

# date_str1 = "2026-03-01" 
# date_str2 = "2026-02-15"

# dt1 = datetime.strptime(date_str1 , "%Y-%m-%d")
# dt2 = datetime.strptime(date_str2 , "%Y-%m-%d")

# result = dt1 > dt2

# print(result)

# from datetime import datetime

# date_str = "2026-03-15"

# dt = datetime.strptime(date_str, "%Y-%m-%d")

# if dt.weekday() == 6:
#     print(f"Day Name: {dt.strftime('%A')}")


# 2026-03-15  is sunday and weekend 

# date_str = "2026-03-15"

# dt = datetime.strptime(date_str, "%Y-%m-%d")

# day_name = dt.strftime("%A")

# if dt.weekday() >= 5:
#     day_type = "Weekend"
# else:
#     day_type = "Weekday"

# print(f"{date_str} is a {day_name} and it is a {day_type}")


# get todays date Take today’s date
# Print the next 5 business days
# Skip weekends


# today_day= datetime.today()

# print("Today", today_day.strftime("%Y-%m-%d"))

# business_days = 0 
# current_Day = today_day

# print("\n next  5  business day" )

# while business_days <5:
   

#     if current_Day.weekday() < 5:
#         print(current_Day.strftime("%Y-%m-%d") , "-" , current_Day.strftime("%A"))
#         business_days += 1 
#     current_Day = current_Day + timedelta(days = 1)

# sales_data = []

# # with open("sales_with_data.csv" , "r") as f :
   


# #  parsing date time 
#     print("\n parsing date time ")

#     reader = csv.DictReader(f)

#     for row in reader:
#         sales_data.append(row)
# print(sales_data)


# for r in sales_data:
#     dtt = datetime.strptime((r["date"]) , "%Y-%m-%d")
#     print(dtt)

# today = datetime.strptime("2026-03-20" , "%Y-%m-%d")
# cutoffday = today - timedelta(days = 30)

# total = 0 
# for r in sales_data:
#     sale_date = datetime.strptime(r["date"], "%Y-%m-%d" )
#     if sale_date >= cutoffday:
        
#         revenue_cal =  int(r["price"]) * int(r["quantity"])
#         total = total + revenue_cal
        

# print(f"the total is {total}")


# “Total revenue for the previous calendar month (not last 30 days).”


# sales_data = []

# with open("sales_with_data.csv" , "r") as f :
   


#  parsing date time 
#     print("\n parsing date time ")

#     reader = csv.DictReader(f)

#     for row in reader:
#         sales_data.append(row)
# print(sales_data)

# # today date 
# today = datetime.strptime("2026-03-20", "%Y-%m-%d")

# # first day of current month 
# first_day_of_month = today.replace(day=1)

# # last_day_of_previous_month
# previous_month_end = first_day_of_month- timedelta(days = 1)

# previous_month_start = previous_month_end.replace(day=1)

# print(f"previous month end is {previous_month_end}")


# print(f"previous month start is {previous_month_start}")

# total_per_month = 0 

# for r in sales_data:
#     sale_date = datetime.strptime(r["date"], "%Y-%m-%d")

#     if previous_month_start <= sale_date <= previous_month_end:
#         revenue = int(r["quantity"]) * int(r["price"])
#         total_per_month = revenue + total_per_month 

# print(f"the total rvenue for previous month is {total_per_month}")



#  w
# reading and creating a sales_data fro sales_data.csv
sales_data = []
with open("sales_with_data.csv", "r" ) as  f :
    reader = csv.DictReader(f)
    for row in reader:
        sales_data.append(row)


# cpmoputing today , forst day of month , preious month end and previous month stasrt 


today = datetime.strptime("2026-03-20", "%Y-%m-%d")


first_day_of_month = today.replace(day=1)

previous_month_end = first_day_of_month - timedelta(days=1)

previous_month_start = previous_month_end.replace(day=1)

print(f"{today}, {previous_month_start} , {first_day_of_month} , {previous_month_end}")

# creating a rwo block for previous month calculation 

report_rows = []
total_prev_month = 0 

for r in sales_data:
    sale_date = datetime.strptime(r["date"], "%Y-%m-%d")
    # now looping over for month calculation 

    if previous_month_start <= sale_date <= previous_month_end:
        
        revenue = int(r["quantity"]) * int(r["price"]) 
        r["revenue"] = revenue
        report_rows.append(r)
        total_prev_month = revenue + total_prev_month

print(report_rows)
print(total_prev_month)

fieldnames = ["order_id", "customer", "product", "quantity", "price", "date", "revenue"]
       
with open("sales_report.csv", "w" , newline ="" , encoding = "utf-8") as f :
    
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(report_rows)
print("✅ sales_report.csv created")
print("Total revenue:", total_prev_month)
    
    









    