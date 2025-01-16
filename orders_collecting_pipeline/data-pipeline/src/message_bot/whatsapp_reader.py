from twilio.rest import Client

def read_whatsapp_messages():
    # Configurar Twilio
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token) # <--- ¿introducir WA business?

    messages = client.messages.list()

    whatsapp_messages = []
    for message in messages:
        if message.direction == 'inbound' and message.from_.startswith('whatsapp:'):
            whatsapp_messages.append((message.from_, message.body))
    return whatsapp_messages