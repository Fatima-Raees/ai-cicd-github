"""Simple utility functions used for CI and performance-demo style testing."""

import re
from typing import Iterable


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def multiple(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b


def calculate_average(values: Iterable[int | float]) -> float:
    """Return the arithmetic mean for a collection of numeric values."""
    items = list(values)
    if not items:
        raise ValueError("average of empty list is not defined")
    return sum(items) / len(items)


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring case and punctuation."""
    normalized = re.sub(r"[^a-z0-9]", "", s.lower())
    return normalized == normalized[::-1]


def normalize_text(s: str) -> str:
    """Trim, lowercase, and collapse whitespace in a string."""
    return " ".join(s.strip().lower().split())


def process_batch(values: Iterable[int]) -> list[int]:
    """Return a list with each value doubled; used as a batch-processing smoke test."""
    return [value * 2 for value in values]
