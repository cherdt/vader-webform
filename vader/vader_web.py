"""VADER sentiment analyzer webform/mini web application."""
import json
import nltk.data
from flask import Flask
from flask import escape
from flask import Markup
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


def score_sentences_to_html(text):
    """Score sentences using VADER and markup output with HTML and CSS

    Arguments: text -- user-submitted text
    """
    html = []
    scored_sentences = score_sentences(text)

    for item in scored_sentences:
        css_class = 'neutral'
        if item['score'] > 0:
            css_class = 'positive'
        elif item['score'] < 0:
            css_class = 'negative'
        span = (Markup('<span class="' + css_class + '">') +
                escape(item['sentence']) +
                Markup('<sup>' + format(item['score'], '.2f') +
                '</sup></span>'))
        html.append(span)

    return Markup(' '.join(html))


def score_text(text):
    """Given text, return the score of the text

    Arguments:
    text -- some text
    """
    return sid.polarity_scores(text.replace('#', ''))


@app.route("/", methods=['GET', 'POST'])
def index():
    """Display the index page of the app"""
    input_text = ''
    scored_text = ''
    aggregate_score = ''

    if request.form.get('input_text'):
        input_text = request.form.get('input_text')
        scored_text = score_sentences_to_html(input_text)
        aggregate_score = str(score_text(input_text)['compound'])

    return render_template('index.html',
                            input_text=input_text,
                            scored_text=scored_text,
                            aggregate_score=aggregate_score)


@app.route("/api")
def score_input():
    """Process API requests to the app"""
    text = request.args.get('text')

    return json.dumps(score_text_and_summary(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
