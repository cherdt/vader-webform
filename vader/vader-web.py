import json
import nltk.data
from flask import Flask
from flask import escape
from flask import request
#from flask import send_static_file
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

splitter = nltk.data.load('tokenizers/punkt/english.pickle')
sid = SentimentIntensityAnalyzer()


def score(text):
    return sid.polarity_scores(text)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/api")
def score_input():
    text = request.args.get('text')
    scored_values = {}
    scored_values['sentences'] = []

    # Analyzing scores for entire text, in aggregate
    scores = score(text)
    scored_values['aggregate_score'] = scores['compound']

    # Analyzes scores per sentence
    for sentence in splitter.tokenize(text):
        scores = score(sentence)
        scored_values['sentences'].append({'sentence': escape(sentence), 'score': scores['compound']})

    return json.dumps(scored_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0') 


