import sys
import csv
from datetime import datetime , timedelta

def convert_csv_to_list(filename : str  ) -> list[dict]:
    sales_data = []

    with open(filename , "r" , encoding="utf-8") as f :
        reader = csv.DictReader(f)

        for row in reader:
            sales_data.append(row)
    return sales_data   


sales = convert_csv_to_list("sales_with_data.csv")



# Build the “previous month range” function
def previous_month_range(today : datetime) -> tuple[datetime, datetime]:
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    
    first_day_of_this_month = today.replace(day=1)
    prev_month_end = first_day_of_this_month - timedelta(days=1)
    prev_month_start = prev_month_end.replace(day=1)
        
    return prev_month_start, prev_month_end
# testing it 
# today = datetime.strptime("2026-03-20", "%Y-%m-%d")
# start, end = previous_month_range(today)
# print(start, end)


def build_prev_month_report(sales_data:list[dict],start:datetime, end : datetime ) -> tuple[list[dict], int] : 
    total = 0 
    report_rows = []

    for r in sales_data:
        sale_date = datetime.strptime(r["date"], "%Y-%m-%d")


        if start <= sale_date <= end:
            revenue = int(r["quantity"]) * int(r["price"])
            out = dict(r)          # copy
            out["revenue"] = revenue

            report_rows.append(out)
            total += revenue

    return report_rows, total


def revenue_per_product(rows: list[dict]) -> dict[str, int]:
    revenue_map = {}

    for r in rows:
        product = r["product"]
        revenue = r["revenue"]

        if product not in revenue_map:
            revenue_map[product] = 0

        revenue_map[product] += revenue

    return revenue_map

def top_products(product_revenue: dict[str, int]) -> list[tuple[str, int]]:
    sorted_products = sorted(
        product_revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_products

def revenue_per_customer(rows: list[dict]) -> dict[str, int]:
    revenue_map = {}

    for r in rows:
        customer = r["customer"]
        revenue = r["revenue"]

        if customer not in revenue_map:
            revenue_map[customer] = 0

        revenue_map[customer] += revenue

    return revenue_map

def write_report(filename: str, report_rows: list[dict]) -> None:
    fieldnames = ["order_id", "customer", "product", "quantity", "price", "date", "revenue"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)


def main(input_file: str, output_file: str) -> None:
    today = datetime.now()
    # datetime.strptime("2026-03-20", "%Y-%m-%d")
    start, end = previous_month_range(today)
    print("Previous month range:", start, end)

    sales = convert_csv_to_list(input_file)
    report_rows, total = build_prev_month_report(sales, start, end)

    product_revenue = revenue_per_product(report_rows)
    print("Revenue per product:", product_revenue)
    sorted_products = top_products(product_revenue)
    print("Top products:", sorted_products)

    top_product = sorted_products[0]
    print("Top product:", top_product)

    write_report(output_file, report_rows)

    print("Total revenue:", total)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 sales_pipeline_v1.py <input_file> <output_file>")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)