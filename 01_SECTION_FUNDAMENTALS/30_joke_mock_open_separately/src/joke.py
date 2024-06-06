"""Joke"""

from pyboxen import boxen
from rich.console import Console

console = Console()
from .api_joke import get_joke


def len_joke() -> int:
    """get length"""
    # This is where get_joke() is called

    the_joke = get_joke()
    console.print("\n\t[blue]in joke.py[/]", the_joke, len(the_joke))
    return len(the_joke)