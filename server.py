"""Flask web application for emotion detection."""

from flask import Flask, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Return detected emotions for the supplied ``textToAnalyze`` value."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if request.method == "POST":
        body = request.get_json(silent=True) or {}
        text_to_analyze = body.get("textToAnalyze", text_to_analyze)

    if not text_to_analyze or not text_to_analyze.strip():
        return jsonify({"error": "Please provide text to analyze."}), 400

    return jsonify(emotion_detector(text_to_analyze))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
