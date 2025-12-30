from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # We return a simple string instead of render_template to avoid missing file errors
    return "Secure Software Design Project is Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
