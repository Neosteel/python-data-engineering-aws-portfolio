import csv
from datetime import datetime

input_file = "input/sales_project_data.csv"


def load_sales_data(file_path):
    rows = []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows


def clean_sales_data(rows):
    clean_rows = []
    invalid_count = 0

    for row in rows:
        try:
            cleaned_row = {
                "order_id": int(row["order_id"]),
                "customer": row["customer"],
                "product": row["product"],
                "quantity": int(row["quantity"]),
                "price": float(row["price"]),
                "date": datetime.strptime(row["date"], "%Y-%m-%d")
            }

            clean_rows.append(cleaned_row)

        except ValueError:
            invalid_count += 1

    return clean_rows, invalid_count


def filter_sales_data(rows, mode, reference_date):
    filtered_rows = []

    if mode == "prev_month":
        for row in rows:
            if row["date"].year == 2026 and row["date"].month == 2:
                filtered_rows.append(row)

    elif mode == "last_30_days":
        for row in rows:
            difference_date = (reference_date - row["date"]).days

            if 0 <= difference_date <= 30:
                filtered_rows.append(row)

    return filtered_rows


def calculate_total_revenue(rows):
    total_revenue = 0

    for row in rows:
        row_revenue = row["price"] * row["quantity"]
        total_revenue += row_revenue

    return total_revenue


def calculate_revenue_by_product(rows):
    revenue_by_product = {}

    for row in rows:
        product = row["product"]
        row_revenue = row["quantity"] * row["price"]

        if product in revenue_by_product:
            revenue_by_product[product] += row_revenue
        else:
            revenue_by_product[product] = row_revenue

    return revenue_by_product


def calculate_revenue_by_customer(rows):
    revenue_by_customer = {}

    for row in rows:
        customer = row["customer"]
        row_revenue = row["quantity"] * row["price"]

        if customer in revenue_by_customer:
            revenue_by_customer[customer] += row_revenue
        else:
            revenue_by_customer[customer] = row_revenue

    return revenue_by_customer


def write_report_to_csv(rows, output_file):
    fieldnames = ["order_id", "customer", "product", "quantity", "price", "date"]

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            output_row = {
                "order_id": row["order_id"],
                "customer": row["customer"],
                "product": row["product"],
                "quantity": row["quantity"],
                "price": row["price"],
                "date": row["date"].strftime("%Y-%m-%d")
            }

            writer.writerow(output_row)


sales_data = load_sales_data(input_file)
clean_data, invalid_count = clean_sales_data(sales_data)

reference_date = datetime(2026, 3, 31)

prev_month_data = filter_sales_data(clean_data, "prev_month", reference_date)
last_30_days_data = filter_sales_data(clean_data, "last_30_days", reference_date)

prev_month_revenue = calculate_total_revenue(prev_month_data)
last_30_days_revenue = calculate_total_revenue(last_30_days_data)

prev_month_product_revenue = calculate_revenue_by_product(prev_month_data)
last_30_days_product_revenue = calculate_revenue_by_product(last_30_days_data)

prev_month_customer_revenue = calculate_revenue_by_customer(prev_month_data)
last_30_days_customer_revenue = calculate_revenue_by_customer(last_30_days_data)

write_report_to_csv(prev_month_data, "output/prev_month_report.csv")
write_report_to_csv(last_30_days_data, "output/last_30_days_report.csv")

print("Invalid row count:", invalid_count)
print("Previous month total revenue:", prev_month_revenue)
print("Last 30 days total revenue:", last_30_days_revenue)
print("Previous month revenue by product:", prev_month_product_revenue)
print("Last 30 days revenue by product:", last_30_days_product_revenue)
print("Previous month revenue by customer:", prev_month_customer_revenue)
print("Last 30 days revenue by customer:", last_30_days_customer_revenue)
print("Filtered reports written successfully.")