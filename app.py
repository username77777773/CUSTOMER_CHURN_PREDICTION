from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

# Initialize Flask app
app = Flask(__name__)

# Set up Ngrok to make the app accessible from the internet
run_with_ngrok(app)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the 'index.html' file

if __name__ == '__main__':
    app.run(debug=True)
