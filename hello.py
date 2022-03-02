from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>' + '<h2>Hola Mundo!</h2>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, DEBUG=True)