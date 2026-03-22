import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze text for emotions using Watson NLP API
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
    
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    # Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to Watson NLP API
    response = requests.post(url, json=payload, headers=headers)
    
    # Convert response text into dictionary using json library
    result = json.loads(response.text)
    
    # Extract required set of emotions and their scores
    emotions = result['emotionPredictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find dominant emotion 
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }