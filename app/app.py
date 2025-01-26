from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SpeakX Flask API (HTTPS Secured!)"
@app.route('/status')
def status():
    jsonify({
        "status": "API is up and Running"
    })
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
