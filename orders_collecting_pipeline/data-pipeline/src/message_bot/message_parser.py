import re
from models.order import Order

def parse_message(sender, body):
    # Extraer información del mensaje usando expresiones regulares
    customer_name = re.search(r"Customer Name: (.*)", body).group(1)
    clothing_model = re.search(r"Clothing Model: (.*)", body).group(1)
    color = re.search(r"Color: (.*)", body).group(1)
    size = re.search(r"Size: (.*)", body).group(1)

    # Crear una instancia de Order
    return Order(customer_name, clothing_model, color, size)