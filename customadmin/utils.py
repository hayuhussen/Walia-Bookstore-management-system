# import requests

# def send_telegram_message(message):
#     token = '7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk'
#     chat_id = '6648120143'
#     url = f'https://api.telegram.org/bot{token}/sendMessage'
    
#     payload = {
#         'chat_id': chat_id,
#         'text': message
#     }
    
#     response = requests.post(url, data=payload)
#     return response




import requests

def send_telegram_message(message, file_path=None):
    token = '7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk'
    chat_id = '6648120143'
    
    # Send the message
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)

    # If there's a file to send, send it
    if file_path:
        url = f'https://api.telegram.org/bot{token}/sendDocument'
        files = {'document': open(file_path, 'rb')}
        payload = {'chat_id': chat_id}
        response = requests.post(url, data=payload, files=files)
    
    return response


