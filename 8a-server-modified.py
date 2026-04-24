from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    text_to_analyse = request.args.get('textToAnalyze')

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyse)

    if "error" in result:
        return jsonify(result), 400

    dominant_emotion = max(result, key=result.get)

    response = {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    