"""Flask web server for the Emotion Detection application."""
from flask import Flask, render_template, request  # pylint: disable=import-error
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyse the emotion of the given text and return a formatted response."""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    output_string = "For the given statement, the system response is "
    output_string += f"anger: {anger}, disgust: {disgust}, fear: {fear}, "
    output_string += f"joy: {joy}, sadness: {sadness}. "
    output_string += f"The dominant emotion is {dominant_emotion}."
    return output_string

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
