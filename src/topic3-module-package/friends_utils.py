"""
friends_utils.py — A standalone module with helper functions for the FRIENDS dataset.

This file demonstrates how a .py file can work both as a runnable script
and as an importable module using the if __name__ == "__main__" pattern.
"""


def format_code(season, episode):
    """Return a human-readable episode code like S01E07."""
    return f"S{season:02d}E{episode:02d}"


def episode_summary(ep):
    """Return a one-line summary from an episode dictionary."""
    code = format_code(ep["season"], ep["episode"])
    return f"{code} - {ep['title']} [{ep['category']}]"


def filter_by_category(episodes, category):
    """Return episodes matching the given category."""
    return [ep for ep in episodes if ep["category"] == category]


def word_count(text):
    """Count the number of words in a text string."""
    return len(text.split())


if __name__ == "__main__":
    print("Running friends_utils.py as a script:")
    print(format_code(1, 1))
    print(format_code(10, 17))
    print(f"Word count of 'Hello world': {word_count('Hello world')}")
