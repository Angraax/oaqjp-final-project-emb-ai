"""Flask web application for emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Return formatted emotion results for the supplied text."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid Input! Please try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the emotion detection user interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
