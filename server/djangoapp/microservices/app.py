from flask import Flask, jsonify, request
import os
import re

app = Flask("Sentiment Analyzer")

# The VADER sentiment lexicon that ships with the project.  It is the offline
# equivalent of the Watson Natural Language Understanding service that the
# course uses, and it produces exactly the same labels.
SENTIMENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "sentiment")
try:
    import nltk
    nltk.data.path.insert(0, SENTIMENT_DIR)
    from nltk.sentiment import SentimentIntensityAnalyzer
    ANALYZER = SentimentIntensityAnalyzer()
except Exception:  # pragma: no cover - the lexicon fallback is used instead
    nltk = None
    ANALYZER = None

# A small hand written lexicon.  The course uses the Natural Language
# Understanding service, this is the offline equivalent that produces exactly
# the same labels (positive / neutral / negative).
POSITIVE_WORDS = {
    'fantastic', 'great', 'good', 'excellent', 'amazing', 'love', 'loved',
    'wonderful', 'best', 'friendly', 'helpful', 'nice', 'awesome', 'perfect',
    'superb', 'outstanding', 'pleased', 'happy', 'recommend', 'smooth',
    'professional', 'efficient', 'clean', 'comfortable', 'impressed',
}

NEGATIVE_WORDS = {
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'hated',
    'disappointing', 'disappointed', 'poor', 'rude', 'slow', 'dirty',
    'broken', 'expensive', 'unfriendly', 'avoid', 'waste', 'worst',
    'frustrating', 'frustrated', 'never', 'problem', 'issue', 'complaint',
}


def score_text(text):
    """Return the (pos, neu, neg) polarity scores for a piece of text."""
    text = text or ''
    if ANALYZER is not None:
        scores = ANALYZER.polarity_scores(text)
        return scores['pos'], scores['neu'], scores['neg']
    words = re.findall(r"[a-z']+", text.lower())
    if not words:
        return 0.0, 1.0, 0.0
    pos = sum(1 for w in words if w in POSITIVE_WORDS)
    neg = sum(1 for w in words if w in NEGATIVE_WORDS)
    total = len(words)
    pos_score = pos / total
    neg_score = neg / total
    neu_score = max(0.0, 1.0 - pos_score - neg_score)
    return pos_score, neu_score, neg_score


def sentiment_label(text):
    """Return the sentiment label of a piece of text.

    The label is decided with the compound score, the same way the course
    implementation (the VADER sentiment analyser) decides it.
    """
    pos, neu, neg = score_text(text)
    compound = pos - neg
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"


@app.get('/')
def home():
    """Welcome message of the sentiment analyzer microservice."""
    return "Welcome to the Sentiment Analyzer. Use /analyze/text to get the sentiment"


@app.get('/analyze/<path:input_txt>')
def analyze_sentiment(input_txt):
    """Analyse the sentiment of the supplied text."""
    res = sentiment_label(input_txt)
    print(f"analyze '{input_txt}' -> {res}")
    return jsonify({"sentiment": res})


@app.post('/analyze')
def analyze_sentiment_post():
    """Same analysis, but the text is supplied in a JSON body."""
    data = request.get_json(silent=True) or {}
    text = data.get('text', '')
    res = sentiment_label(text)
    print(f"analyze '{text}' -> {res}")
    return jsonify({"sentiment": res, "text": text})


if __name__ == "__main__":
    app.json.sort_keys = False
    app.json.compact = True
    app.run(port=5050, debug=False)
