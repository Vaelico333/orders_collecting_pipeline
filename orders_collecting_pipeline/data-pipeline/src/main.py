def main():
    import pandas as pd
    from data_processing.process_orders import process_order
    from models.order import Order

    # Example of receiving a customer order
    customer_name = input("Nombre o empresa: ")
    clothing_model = input("Modelo de prenda: ")
    color = input("Color: ")
    size = input("Talla: ")
    number = input("Cantidad: ")

    # Create an Order instance
    order = Order(customer_name, clothing_model, color, size)

    # Process the order and store it in the CSV file
    process_order(customer_name, clothing_model, color, size, number)

if __name__ == "__main__":
    main()

'''import schedule
import time
from email_bot.email_reader import read_emails
from email_bot.email_parser import parse_email
from data_processing.process_orders import process_order

def job():
    emails = read_emails()
    whatsapp_messages = read_whatsapp_messages()
    facebook_messages = read_facebook_messages()    
    for subject, body in emails:
        order = parse_email(subject, body)
        process_order(order.customer_name, order.clothing_model, order.color, order.size)
    for sender, body in whatsapp_messages + facebook_messages:
        order = parse_message(sender, body)
        process_order(order.customer_name, order.clothing_model, order.color, order.size)

def main():
    # Programar el bot para que se ejecute dos veces al día
    schedule.every().day.at("07:00").do(job)
    schedule.every().day.at("18:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()'''