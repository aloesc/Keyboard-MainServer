import keyboard
import json

from flask import Flask, request

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def handle_get():
    return "Hello, world! This is a GET response."

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_data()
    decoded_data = json.loads(data.decode())

    if "key" in decoded_data:
        keyboard.press_and_release(decoded_data["key"])
        print(f'{decoded_data["key"]} pressed')
        return "pressed"
    else:
        return "connected"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
