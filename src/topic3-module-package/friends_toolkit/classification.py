"""
classification.py — Simple keyword-based episode classifier.
"""

from .preprocessing import preprocess

KEYWORD_SETS = {
    "Romance": {"love", "kiss", "romance", "couple", "feelings", "relationship"},
    "Career": {"job", "career", "work", "boss", "promotion", "interview", "chef"},
    "Family": {"baby", "pregnant", "family", "father", "wedding", "parents", "birth"},
    "Friendship": {"friends", "group", "gang", "together", "support", "bond"},
}


def classify_episode(ep):
    """Predict the category of an episode based on keyword matching."""
    tokens = set(preprocess(ep["description"]))
    best_category = "Friendship"
    best_score = 0
    for category, keywords in KEYWORD_SETS.items():
        score = len(tokens & keywords)
        if score > best_score:
            best_score = score
            best_category = category
    return best_category
