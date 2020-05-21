from PIL import Image
import pytesseract
from flask import (Flask, jsonify, request)
from urllib.request import urlopen


app = Flask(__name__)


@app.route("/image_to_text")
def convert_image_to_text():
    # accept json structure {"image_url", "http://path-to-image.jpg"}
    image_url = request.get_json().get("image_url", "")
    if image_url:
        image = urlopen(image_url)
        try:
            # convert the image to text
            converted_text = pytesseract.image_to_string(Image.open(image))
        except Exception as err:
            return jsonify({"text": str(err)})
        if converted_text:
            return jsonify({"text": converted_text})
        return jsonify({"text": "Fail to generate text"})
    return jsonify({"message": "Image URL is missing"})


if __name__ == "__main__":
    # start he development server
    app.run(debug=True, host='localhost', port=3000)

