from flask import Flask, request, jsonify, send_file, render_template

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] != 0:
            return render_template("index.html", message="Negative Feedback ☹️☹️")
        else:
            return render_template("index.html", message="Positive Feed back 😁😁")
    return render_template("index.html")



