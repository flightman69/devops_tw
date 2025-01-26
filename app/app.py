from flask import Flask , send_from_directory, render_template,jsonify, Response
import requests
import os
import re
import random

jokes = [
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
    "I don't always test my code, but when I do, I do it in production.",
    "Why do programmers prefer dark mode? Because light mode is for people who don’t code.",
    "I have a joke about UDP, but you probably won't get it.",
    "My code works perfectly... until I try to run it.",
    "Why did the developer go broke? Because he used up all his cache.",
    "I spent hours debugging my code... It was the semicolon all along."
]


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/status')
def status():
    return {
        "status": "active",
        "version": "1.0.0",
        "environment": "production"
    }, 200


@app.route('/health')
def health_check():
    return {"status": "healthy"}, 200


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return data, 200


@app.route('/joke')
def get_joke():
    joke = random.choice(jokes)
    return {"joke": joke}, 200


@app.route('/pic')
def show_pic():
    
    images_folder = 'images'
    image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    
    
    random_image = random.choice(image_files)
    
    
    return send_from_directory(images_folder, random_image)

@app.route('/weather')
def get_weather():
    
    url = 'https://wttr.in'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_info = re.sub(r'\x1b\[[0-9;]*m', '', response.text)
            return Response(weather_info, content_type='text/plain; charset=utf-8'), 200
        else:
            return "Error: Failed to fetch weather data", 500
    except Exception as e:
        return f"Error: {str(e)}", 500
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
