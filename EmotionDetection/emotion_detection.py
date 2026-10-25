"""Emotion detection client for the Watson NLP service."""

from typing import Any, Dict, Optional

import requests


WATSON_EMOTION_URL = "https://sn-watson-emotion.labs.coursera.org/emotion"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze: str) -> Dict[str, Optional[Any]]:
    """Detect emotions in text and return scores plus the dominant emotion.

    A failed or invalid request returns a consistent empty result so callers
    can distinguish it from a successful prediction.
    """
    response = requests.post(
        WATSON_EMOTION_URL,
        json={"text": text_to_analyze},
        timeout=30,
    )

    if response.status_code == 400:
        return {emotion: None for emotion in EMOTIONS} | {"dominant_emotion": None}

    response.raise_for_status()
    payload = response.json()
    emotion_scores = payload["emotionPredictions"][0]["emotion"]
    scores = {emotion: emotion_scores[emotion] for emotion in EMOTIONS}
    scores["dominant_emotion"] = max(
        EMOTIONS,
        key=lambda emotion: emotion_scores[emotion],
    )
    return scores
