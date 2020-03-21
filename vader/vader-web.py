import json
import nltk.data
from flask import Flask
from flask import escape
from flask import render_template
from flask import request
#from flask import send_static_file
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

splitter = nltk.data.load('tokenizers/punkt/english.pickle')
sid = SentimentIntensityAnalyzer()


def score_text_and_summary(text):
    """Given a block of text, return scores for sentences and combined text

    Arguments:
    text -- a block of text
    """
    scored_values = {}
    scored_values['sentences'] = []

    # Analyzing scores for entire text, in aggregate
    scores = score_text(text)
    scored_values['aggregate_score'] = scores['compound']

    # Analyzes scores per sentence
    scored_values['sentences'] = score_sentences(text)

    return scored_values


def score_sentences(text):
    """Given a block of text, return scores for each consituent sentence

    Arguments:
    text -- a block of text
    """
    scored_sentences = []

    # Analyzes scores per sentence
    for sentence in splitter.tokenize(text):
        scores = score_text(sentence)
        scored_sentences.append({'sentence': escape(sentence), 'score': scores['compound']})

    return scored_sentences


def score_text(text):
    """Given text, return the score of the text

    Arguments:
    text -- some text
    """
    return sid.polarity_scores(text.replace('#', ''))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api")
def score_input():
    text = request.args.get('text')

    return json.dumps(score_text_and_summary(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0') 


