"""Unit tests for the emotion detector."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for each required dominant emotion."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_detects_each_dominant_emotion(self, post):
        """Identify anger, disgust, fear, joy, and sadness."""
        for dominant_emotion in ("anger", "disgust", "fear", "joy", "sadness"):
            scores = {emotion: 0.01 for emotion in (
                "anger", "disgust", "fear", "joy", "sadness"
            )}
            scores[dominant_emotion] = 0.9
            post.return_value = Mock(
                status_code=200,
                text=json.dumps({
                    "emotionPredictions": [{"emotion": scores}]
                }),
            )

            result = emotion_detector(f"I feel {dominant_emotion}")

            self.assertEqual(result["dominant_emotion"], dominant_emotion)
            self.assertEqual(set(result), {
                "anger", "disgust", "fear", "joy", "sadness",
                "dominant_emotion",
            })

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_empty_result_for_bad_request(self, post):
        """Return empty values when Watson rejects the request."""
        post.return_value = Mock(status_code=400)

        result = emotion_detector("invalid request")

        self.assertEqual(result["dominant_emotion"], None)
        self.assertTrue(all(result[emotion] is None for emotion in (
            "anger", "disgust", "fear", "joy", "sadness"
        )))


if __name__ == "__main__":
    unittest.main()
