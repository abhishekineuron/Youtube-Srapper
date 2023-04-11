#It's a Jupyter File Try to Run it in jupyter notebook

from flask import Flask, jsonify
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app)

@app.route('/get_video_titles', methods=['GET'])
def get_video_titles():
    input_text = 'PW-Foundation'  # YouTube channel name
    url = f'https://www.youtube.com/@{input_text}/videos'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url, headers=headers)
    response_text = response.text

    vid_titles = re.findall('"title":{"runs":\[{"text":"(.*?)"', response_text) # Use regular expression to extract video titles

    return jsonify({'video_titles': vid_titles})

if __name__ == '__main__':
    app.run(debug=True)
