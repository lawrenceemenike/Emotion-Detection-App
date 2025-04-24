import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=input_json, headers=headers)
        
        # Handle 400 status code from server (invalid input)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
        response.raise_for_status()  # Raise for other HTTP errors
        
        response_dict = json.loads(response.text)
        emotion_data = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        emotion_scores = {
            'anger': emotion_data.get('anger', 0),
            'disgust': emotion_data.get('disgust', 0),
            'fear': emotion_data.get('fear', 0),
            'joy': emotion_data.get('joy', 0),
            'sadness': emotion_data.get('sadness', 0)
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        return {**emotion_scores, 'dominant_emotion': dominant_emotion}
        
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error processing request: {e}")
        return None
