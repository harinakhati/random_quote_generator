"""
A simple FastAPI app that serves random quotes.
You can get a random quote or filter by category.
"""

import random

from fastapi import FastAPI, Query

app = FastAPI(title="Random Quote Generator")

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
    """
    Return a random quote.
    
    If a category is provided, return a random quote from that category.
    If no matching quote is found, return a default message.
    """
    if category:
        filtered = [q for q in QUOTES if q["category"] == category.lower()]
        return random.choice(filtered) if filtered else {"text": "No quote found.",
                                                          "category": category}
    return random.choice(QUOTES)

@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"message": "Welcome to the Random Quote Generator!"}

@app.get("/quote")
def read_quote(category: str = Query(None, description=
                                     "Filter by category: motivation, humor, etc.")):
    """
    Return a random quote, optionally filtered by category.
    
    Args:
        category (str, optional): Quote category to filter by.
        
    Returns:
        dict: A quote dictionary containing 'text' and 'category'.
    """
    return get_random_quote(category)
