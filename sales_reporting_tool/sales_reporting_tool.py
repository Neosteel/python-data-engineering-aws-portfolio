import csv
from datetime import datetime


class SalesReportingTool:
    def __init__(self, input_file, reference_date):
        self.input_file = input_file
        self.reference_date = reference_date

    def load_sales_data(self):
        rows = []

        with open(self.input_file, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        return rows

    def clean_sales_data(self, rows):
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

    def filter_sales_data(self, rows, mode):
        filtered_rows = []

        if mode == "prev_month":
            previous_month = self.reference_date.month - 1
            previous_year = self.reference_date.year

            if previous_month == 0:
                previous_month = 12
                previous_year -= 1

            for row in rows:
                if row["date"].year == previous_year and row["date"].month == previous_month:
                    filtered_rows.append(row)

        elif mode == "last_30_days":
            for row in rows:
                difference_date = (self.reference_date - row["date"]).days

                if 0 <= difference_date <= 30:
                    filtered_rows.append(row)

        return filtered_rows

    def calculate_total_revenue(self, rows):
        total_revenue = 0

        for row in rows:
            row_revenue = row["price"] * row["quantity"]
            total_revenue += row_revenue

        return total_revenue

    def calculate_revenue_by_product(self, rows):
        revenue_by_product = {}

        for row in rows:
            product = row["product"]
            row_revenue = row["quantity"] * row["price"]

            if product in revenue_by_product:
                revenue_by_product[product] += row_revenue
            else:
                revenue_by_product[product] = row_revenue

        return revenue_by_product

    def calculate_revenue_by_customer(self, rows):
        revenue_by_customer = {}

        for row in rows:
            customer = row["customer"]
            row_revenue = row["quantity"] * row["price"]

            if customer in revenue_by_customer:
                revenue_by_customer[customer] += row_revenue
            else:
                revenue_by_customer[customer] = row_revenue

        return revenue_by_customer

    def write_report_to_csv(self, rows, output_file):
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

    def get_output_file_name(self, mode):
        if mode == "prev_month":
            return "output/prev_month_report.csv"
        elif mode == "last_30_days":
            return "output/last_30_days_report.csv"

    def run(self):
        sales_data = self.load_sales_data()
        clean_data, invalid_count = self.clean_sales_data(sales_data)

        mode = input("Enter mode (prev_month / last_30_days): ").strip()

        if mode not in ["prev_month", "last_30_days"]:
            print("Invalid mode. Please enter 'prev_month' or 'last_30_days'.")
            return

        filtered_data = self.filter_sales_data(clean_data, mode)
        total_revenue = self.calculate_total_revenue(filtered_data)
        product_revenue = self.calculate_revenue_by_product(filtered_data)
        customer_revenue = self.calculate_revenue_by_customer(filtered_data)

        output_file = self.get_output_file_name(mode)
        self.write_report_to_csv(filtered_data, output_file)

        print("\nMode selected:", mode)
        print("Invalid row count:", invalid_count)
        print("Total revenue:", total_revenue)
        print("Revenue by product:", product_revenue)
        print("Revenue by customer:", customer_revenue)
        print("Report written to:", output_file)


tool = SalesReportingTool(
    input_file="input/sales_project_data.csv",
    reference_date=datetime(2026, 3, 31)
)

tool.run()