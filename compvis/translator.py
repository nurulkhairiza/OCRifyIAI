import requests, uuid

available_languages = [
    {'id': 'en', 'name': 'English'},
    {'id': 'id', 'name': 'Indonesian'},
    {'id': 'de', 'name': 'Germany'},
    {'id': 'it', 'name': 'Italian'},
    {'id': 'fr', 'name': 'French'},
    {'id': 'zh-Hans', 'name': 'Chinese'},
    {'id': 'ja', 'name': 'Japanese'},
]

def translate(text, translate_from, translate_to):
    # Add your key and endpoint
    key = '5a7f1acf4c6847a6b2e26b74835afd80'
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = 'eastus'
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': translate_from,
        'to': [translate_to]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    translated = response[0]['translations'][0]['text']

    return translated

