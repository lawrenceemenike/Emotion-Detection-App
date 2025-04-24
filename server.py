from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Process text and return detected emotions with formatted response.
    Handles invalid text inputs where dominant_emotion is None.
    """
    # Get the text from the request
    text_to_analyze = request.json.get("text", "")
    
    # Call the emotion_detector function to analyze the text
    result = emotion_detector(text_to_analyze)
    
    # Handle complete processing failures
    if result is None:
        return jsonify({
            "response": "Error processing request. Please try again."
        }), 500
    
    # Extract emotion scores and dominant emotion
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]
    
    # Handle invalid text inputs (blank or unprocessable)
    if dominant_emotion is None:
        return jsonify({
            "response": "Invalid text! Please try again!"
        }), 400
    
    # Format successful response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
