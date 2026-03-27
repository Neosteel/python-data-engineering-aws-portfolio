import csv
from datetime import datetime

input_file = "input/sales_project_data.csv"


def load_sales_data(file_path):
    """loading the csv file using dictreader and then converting the csv into doctionarie and then using the key pairs to create a dict of keypair values """
    rows =[]

    with open(file_path,"r",newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)
    return rows




def clean_sales_data(rows):
    """this fuctino will use the rows oto clean one by one 
    will use the try catch and then convert the rows """
    clean_rows = []
    invalid_count = 0 

    for row in rows:
        try:
            cleaned_row = {
                "order_id" :  int(row["order_id"]),
                "customer" : row["customer"],
                "product" :row["product"],
                "quantity" : int(row["quantity"]),
                "price" :float(row["price"]),
                "date" : datetime.strptime(row["date"], "%Y-%m-%d")


            }

            clean_rows.append(cleaned_row)
        except ValueError:
            invalid_count += 1

    return clean_rows,invalid_count


sales_data = load_sales_data(input_file)
clean_data, invalid_count = clean_sales_data(sales_data) 



for r in clean_data:
    print(r)

print("Invalid row count:", invalid_count)





