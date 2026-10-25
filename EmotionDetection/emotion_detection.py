"""Emotion detection client for the Watson NLP service."""

import json
import requests


WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Detect emotions in text and return scores plus the dominant emotion."""
    headers = {"grpc-metadata-mm-model-id": WATSON_MODEL_ID}
    request_body = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(
        WATSON_EMOTION_URL,
        json=request_body,
        headers=headers,
        timeout=30,
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    payload = json.loads(response.text)
    emotion_scores = payload["emotionPredictions"][0]["emotion"]
    emotion_scores["dominant_emotion"] = max(
        EMOTIONS,
        key=lambda emotion: emotion_scores[emotion],
    )
    return emotion_scores
