from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Flask route for emotion detection
    Processes text input and returns formatted emotion analysis
    """
    if request.method == 'POST':
        # Get the text from the request
        text_to_analyze = request.form.get('text', '')
        
        if not text_to_analyze:
            return jsonify({'error': 'No text provided'}), 400
        
        # Call the emotion_detector function
        result = emotion_detector(text_to_analyze)
        
        # Check for invalid input (if API returns None or error)
        if result.get('dominant_emotion') is None:
            return jsonify({'error': 'Invalid text input'}), 400
        
        # Format the output as requested
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        
        return jsonify({
            'result': result,
            'formatted_response': formatted_response
        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)