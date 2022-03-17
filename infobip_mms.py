import requests
import json

data = {
    "head": {
        "from": {YOUR NUMBER HERE},
        "to": {MOBILE YOU ARE SENDING TOO},
        "subject": "my pretty kitty",
    },
    "text": "My Pretty Pussy cat",
    "contentLinks": [
        {
                    "contentType": "image/jpeg",
                    "contentId": "my_pretty_kitty",
                    "contentUrl": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Orange_tabby_cat.jpg"
        }
    ]
}
header = {
    'Authorization': 'App {API KEY}'
}
print(data['head'])

files = {
    'head': (None, json.dumps(data['head']).encode(),'application/json'),
    'text': (None, json.dumps(data['text']).encode(), 'text/plain'),
    'contentLinks': (None, json.dumps(data['contentLinks']).encode(), 'application/json')
}

response = requests.post('https://{CUSTOM URL}/mms/1/single', files=files, headers=header)
print(response)

data = response.content
