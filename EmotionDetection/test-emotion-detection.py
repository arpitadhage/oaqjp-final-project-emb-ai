import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(max(result, key=result.get), "joy")

    def test_anger(self):
        result = emotion_detector("I am angry")
        self.assertEqual(max(result, key=result.get), "anger")

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertEqual(max(result, key=result.get), "sadness")

    def test_fear(self):
        result = emotion_detector("I am afraid")
        self.assertEqual(max(result, key=result.get), "fear")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted")
        self.assertEqual(max(result, key=result.get), "disgust")

if __name__ == '__main__':
    unittest.main()