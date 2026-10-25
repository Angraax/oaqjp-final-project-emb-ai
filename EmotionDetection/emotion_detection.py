"""Emotion detection client for the Watson NLP service."""

import requests


WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.coursera.org/emotionPredict"
)
WATSON_MODEL_HEADER = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze: str) -> dict:
    """Detect emotions in text and return scores plus the dominant emotion."""
    response = requests.post(
        WATSON_EMOTION_URL,
        headers={"grpc-metadata-mm-model-id": WATSON_MODEL_HEADER},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )

    if response.status_code == 400:
        return {
            emotion: None for emotion in EMOTIONS
        } | {"dominant_emotion": None}

    response.raise_for_status()
    payload = response.json()
    emotion_scores = payload["emotionPredictions"][0]["emotion"]
    scores = {
        emotion: emotion_scores[emotion]
        for emotion in EMOTIONS
    }
    scores["dominant_emotion"] = max(
        EMOTIONS,
        key=lambda emotion: emotion_scores[emotion],
    )
    return scores
