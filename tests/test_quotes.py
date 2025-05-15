"""
test_quotes.py

This module contains unit tests for the Random Quote Generator FastAPI application.
It tests functionality from the `quotes` module.
"""

from app.quotes import get_random_quote


def test_get_random_quote_returns_dict():
    """Test that get_random_quote() returns a dictionary with 'text' and 'category' keys."""
    quote = get_random_quote()
    assert isinstance(quote, dict)
    assert "text" in quote
    assert "category" in quote


def test_get_random_quote_with_category():
    """Test that get_random_quote(category='motivation') 
    returns a quote from the specified category."""
    quote = get_random_quote(category="motivation")
    assert quote["category"].lower() == "motivation"
