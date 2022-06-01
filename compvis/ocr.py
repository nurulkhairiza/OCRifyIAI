from array import array
import io
import os
from PIL import Image
import requests
import sys
import time
import json

subscription_key = "d601b76dba21497e8c34527dceace38d"
endpoint = "https://iai-cv.cognitiveservices.azure.com/"

ocr_endpoint = endpoint + 'vision/v3.1/ocr'
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}

#computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def sendOCR(image):
    out = io.BytesIO()
    image.save(out, format = image.format)
    data = out.getvalue()
    read_response = requests.post(ocr_endpoint, headers=headers, data=data)
    read_response.raise_for_status()
    read_response_result = read_response.json()
    textbox_result = ""
    #######################
    # Modify as necessary #
    #######################
    for region in read_response_result['regions']:
        for line in region['lines']:
            for word in line['words']:
                textbox_result = textbox_result + word['text'] + " "
    return textbox_result[:-1]
        

