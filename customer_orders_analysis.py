# customer_orders_analysis.py
# This script analyzes customer orders, classifies customers based on their spending,
# Sample data
customer_names = ["Alice", "Bob", "Charlie", "Diana"]

# Each order is a tuple: (customer_name, product, price, category)
orders = [
    ("Alice", "Laptop", 900, "Electronics"),
    ("Alice", "Headphones", 50, "Electronics"),
    ("Bob", "T-shirt", 20, "Clothing"),
    ("Bob", "Jeans", 40, "Clothing"),
    ("Charlie", "Blender", 70, "Home Essentials"),
    ("Diana", "Smartphone", 600, "Electronics"),
    ("Diana", "Dress", 80, "Clothing"),
    ("Diana", "Vacuum Cleaner", 150, "Home Essentials")
]

# Map customer -> list of products
customer_orders = {}
for name in customer_names:
    customer_orders[name] = []

for order in orders:
    customer, product, price, category = order
    customer_orders[customer].append((product, price, category))

# Product -> category mapping
product_category = {}
for _, product, _, category in orders:
    product_category[product] = category

unique_categories = set(product_category.values())
print("Available Product Categories:", unique_categories)

# Analyze customer spending and classify
customer_total_spend = {}
customer_classification = {}

for customer, items in customer_orders.items():
    total = sum(price for _, price, _ in items)
    customer_total_spend[customer] = total

    if total > 100:
        customer_classification[customer] = "High-Value Buyer"
    elif 50 <= total <= 100:
        customer_classification[customer] = "Moderate Buyer"
    else:
        customer_classification[customer] = "Low-Value Buyer"

print("\nCustomer Spending and Classification:")
for customer in customer_names:
    print(f"{customer}: ${customer_total_spend[customer]} - {customer_classification[customer]}")

# Revenue per category
category_revenue = {}
for _, _, price, category in orders:
    category_revenue[category] = category_revenue.get(category, 0) + price

print("\nTotal Revenue per Category:")
for category, revenue in category_revenue.items():
    print(f"{category}: ${revenue}")

# Unique products
unique_products = set(product for _, product, _, _ in orders)
print("\nUnique Products Purchased:", unique_products)

# Customers who purchased Electronics
electronics_customers = [customer for customer, items in customer_orders.items()
                          if any(category == "Electronics" for _, _, category in items)]
print("\nCustomers who purchased Electronics:", electronics_customers)

# Top 3 highest spenders
top_spenders = sorted(customer_total_spend.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 Highest Spending Customers:")
for name, total in top_spenders:
    print(f"{name}: ${total}")

# Customers who purchased from multiple categories
customer_categories = {}
for customer, items in customer_orders.items():
    cats = set(category for _, _, category in items)
    customer_categories[customer] = cats

multi_category_customers = [customer for customer, cats in customer_categories.items() if len(cats) > 1]
print("\nCustomers who purchased from multiple categories:", multi_category_customers)

# Customers who bought both Electronics and Clothing
both_elec_clothing = [customer for customer, cats in customer_categories.items()
                      if "Electronics" in cats and "Clothing" in cats]
print("\nCustomers who bought both Electronics and Clothing:", both_elec_clothing)

