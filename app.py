from flask import Flask, render_template
from pyngrok import ngrok

app = Flask(__name__, template_folder='/content/CUSTOMER_CHURN_PREDICTION/templates')

# Start ngrok and get the public URL
public_url = ngrok.connect(5000).public_url
print(f"Public URL: {public_url}")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)
