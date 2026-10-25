"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for Watson emotion response formatting."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_formatted_emotions(self, post):
        """Return scores and identify the highest-scoring emotion."""
        response = Mock(status_code=200)
        response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.9,
                        "sadness": 0.04,
                    }
                }
            ]
        }
        post.return_value = response

        result = emotion_detector("I am very happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.9)
        post.assert_called_once()

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
