def get_sort_key(item, sort_key):
    return item[sort_key]


def sort_products(products, sort_key, ascending=True):
    sorted_products = sorted(products, key=get_sort_key_wrapper(sort_key), reverse=not ascending)

    return sorted_products


def get_sort_key_wrapper(sort_key):
    def get_key(item):
        return get_sort_key(item, sort_key)
    return get_key


# Examples
products = [
    {"name": "Product A", "price": 100, "stock": 5},
    {"name": "Product B", "price": 200, "stock": 3},
    {"name": "Product C", "price": 50, "stock": 10}
]
sort_key = "price"
ascending = False

# Sort products
sorted_products = sort_products(products, sort_key, ascending)
print(sorted_products)
