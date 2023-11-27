from menu import products

def calculate_tab(comands: list) -> dict:
    subtotal = 0
    for product in products:
        for comand in comands:
            if comand["_id"] == product["_id"]:
                subtotal += product["price"] * comand["amount"]
    subtotal_formatado = "${:.2f}".format(subtotal)
    return {"subtotal": subtotal_formatado}        