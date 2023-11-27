from menu import products

def get_product_by_id(id: int) -> dict:
    for product in products:
        if product ["_id"] == id:
            return product
    return {}

def get_products_by_type(type: str):
    filtered_products = []
    for product in products:
        if product ["type"] == type:
            filtered_products.append(product)
    return filtered_products    

def add_product(**product_data: dict):
    last_id = 0
    for product in products:
        if product["_id"] > last_id:
            last_id = product["_id"]
    product_data["_id"] = last_id + 1    
    products.append(product_data)
    return product_data