
data = [
    {"product": "A", "sales": 100},
    {"product": "B", "sales": 200},
    {"product": "A", "sales": 50},
    {"product": "C", "sales": 300},
    {"product": "B", "sales": 100},
]

result = {}

# Total sales per product
for person in data:
    product = person["product"]
    sales = person["sales"]

    if product not in result:
        result[product] = 0

    result[product] += sales

# Sorting products by earnings (descending)
sorted_results = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Output
print(sorted_results)

# output: [('B', 300), ('C', 300), ('A', 150)]
