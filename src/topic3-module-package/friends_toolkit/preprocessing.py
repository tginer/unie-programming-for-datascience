"""
preprocessing.py — Text preprocessing functions for episode descriptions.
"""

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "not", "no", "nor",
    "it", "its", "he", "she", "they", "them", "his", "her", "their",
    "this", "that", "these", "those", "who", "whom", "which", "what",
    "when", "where", "how", "all", "each", "every", "both", "few",
    "more", "most", "other", "some", "such", "only", "own", "same",
    "than", "too", "very", "just", "about", "up", "out", "so", "if",
    "from", "into", "through", "during", "before", "after", "above",
    "as", "then", "once", "here", "there", "also", "over",
}


def clean_text(text):
    """Lowercase and strip punctuation from text."""
    text = text.lower()
    cleaned = ""
    for char in text:
        if char.isalnum() or char == " ":
            cleaned += char
    return cleaned


def tokenize(text):
    """Split cleaned text into a list of words."""
    return text.split()


def remove_stop_words(tokens):
    """Filter out stop words from a token list."""
    return [t for t in tokens if t not in STOP_WORDS]


def preprocess(text):
    """Full preprocessing pipeline: clean -> tokenize -> remove stops."""
    return remove_stop_words(tokenize(clean_text(text)))
