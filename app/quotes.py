"""
Random Quote Generator FastAPI application.

Provides endpoints to fetch random quotes, optionally filtered by category.
"""

import random

QUOTES = [
    {"text": "Believe in yourself!", "category": "motivation"},
    {"text": "I'm not lazy, I'm on energy-saving mode.", "category": "humor"},
    {"text": "Do one thing every day that scares you.", "category": "motivation"},
    {"text": "Why don’t scientists trust atoms?"
    "Because they make up everything!",
    "category": "humor"},
    {"text": "Stay hungry. Stay foolish.", "category": "inspiration"},
]

def get_random_quote(category: str = None):
    """Return a welcome message for the API root."""
    if category:
        filtered = [q for q in QUOTES if q["category"] == category.lower()]
        return random.choice(filtered) if filtered else {"text": "No quote found.",
                                                          "category": category}
    return random.choice(QUOTES)
