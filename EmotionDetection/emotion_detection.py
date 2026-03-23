"""
Emotion Detection Module.

This module provides functionality to analyze text for emotions
using the Watson NLP API. It returns emotion scores and identifies
the dominant emotion in the given text.
"""

import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze text for emotions using Watson NLP API.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion.
              Returns None values if input is invalid (status_code 400).
              
              Keys:
                  - anger (float): Anger emotion score
                  - disgust (float): Disgust emotion score
                  - fear (float): Fear emotion score
                  - joy (float): Joy emotion score
                  - sadness (float): Sadness emotion score
                  - dominant_emotion (str): Name of the dominant emotion
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

    # Check status_code for error handling
    if response.status_code == 400:
        # Return dictionary with all values as None for blank/invalid input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert response text into a dictionary using json library
    result = json.loads(response.text)

    # Extract the required set of emotions with their scores
    emotions = result['emotionPredictions'][0]['emotion']

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
