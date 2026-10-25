# Final Project

An AI-based customer-feedback emotion detector built with Python, Watson NLP,
and Flask.

## Run locally

```text
python -m pip install -r requirements.txt
python -m unittest -v
python server.py
```

Then visit:

```text
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20love%20this%20product
```

## Assignment evidence checklist

- Task 1: publish this repository and submit the public `README.md` URL.
- Task 2-3: submit `EmotionDetection/emotion_detection.py` and its test output.
- Task 4: submit `EmotionDetection/__init__.py` and package import output.
- Task 5: submit `test_emotion_detection.py` and passing unit-test output.
- Task 6-7: run `server.py` and capture deployment/error-handling screenshots.
- Task 8: run `pylint server.py EmotionDetection` and submit the perfect score.
