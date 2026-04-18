import json

# description: group sales by city → product → year

data = [
    {"city": "NY", "product": "A", "sales": 100, "year": 2023},
    {"city": "NY", "product": "B", "sales": 200, "year": 2023},
    {"city": "NY", "product": "A", "sales": 50,  "year": 2024},
    {"city": "LA", "product": "A", "sales": 75,  "year": 2023},
    {"city": "LA", "product": "B", "sales": 125, "year": 2024},
    {"city": "LA", "product": "A", "sales": 25,  "year": 2024},
]

sales_by_city_product_year = {}

for person in data:
    city = person["city"]
    product = person["product"]
    sales = person["sales"]
    year = person["year"]

    if city not in sales_by_city_product_year:
        sales_by_city_product_year[city] = {}

    if product not in sales_by_city_product_year[city]:
        sales_by_city_product_year[city][product] = {}

    if year not in sales_by_city_product_year[city][product]:
        sales_by_city_product_year[city][product][year] = 0

    sales_by_city_product_year[city][product][year] += sales

json_output = json.dumps(sales_by_city_product_year, indent=2)
print(json_output)

# output:
# {
#   "NY": {"A": {"2023": 100, "2024": 50}, "B": {"2023": 200}},
#   "LA": {"A": {"2023": 75, "2024": 25}, "B": {"2024": 125}}
# }
