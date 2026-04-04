"""
friends_toolkit — A package for working with the FRIENDS TV series dataset.

This __init__.py file marks the folder as a Python package and controls
what is exposed when someone does `import friends_toolkit`.
"""

from .data import episodes
from .preprocessing import clean_text, preprocess
from .classification import classify_episode
