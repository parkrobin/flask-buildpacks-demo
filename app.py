from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Buildpacks World!'

@app.route('/env')
def show_env():
    return '\n'.join([f'{key}: {value}' for key, value in sorted(os.environ.items())])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)