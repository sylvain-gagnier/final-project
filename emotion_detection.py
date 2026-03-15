import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    #return formatted_response
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    return_object = {
        'anger': emotions['anger'] || 0,
        'disgist': emotions['disgust'] || 0,
        'fear': emotions['fear'] || 0,
        'joy': emotions['joy'] || 0,
        'sadness': emotions['sadness'] || 0
    }
    return return_object