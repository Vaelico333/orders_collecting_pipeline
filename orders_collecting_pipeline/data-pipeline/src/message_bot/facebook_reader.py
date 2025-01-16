import requests

def read_facebook_messages():
    access_token = 'your_access_token'
    page_id = 'your_page_id'
    url = f'https://graph.facebook.com/v12.0/{page_id}/conversations?access_token={access_token}'

    response = requests.get(url)
    conversations = response.json().get('data', [])

    facebook_messages = []
    for conversation in conversations:
        conversation_id = conversation['id']
        messages_url = f'https://graph.facebook.com/v12.0/{conversation_id}/messages?access_token={access_token}'
        messages_response = requests.get(messages_url)
        messages = messages_response.json().get('data', [])
        for message in messages:
            if 'message' in message:
                facebook_messages.append((message['from']['name'], message['message']))
    return facebook_messages