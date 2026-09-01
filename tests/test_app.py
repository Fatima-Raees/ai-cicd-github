"""Portfolio-style tests covering core logic and load-oriented smoke checks."""

import time

import pytest

from app import (
    add,
    calculate_average,
    is_even,
    is_palindrome,
    multiple,
    normalize_text,
    process_batch,
    reverse_string,
)


class TestMath:
    """Unit tests for arithmetic behavior."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_add_zero_identity(self):
        assert add(0, 8) == 8
        assert add(-5, 5) == 0

    def test_multiple(self):
        assert multiple(9, 9) == 81
        assert multiple(-1, 5) == -5
        assert multiple(0, 25) == 0

    def test_calculate_average(self):
        assert calculate_average([10, 20, 30]) == 20
        assert calculate_average([5, 5, 5, 5]) == 5

    def test_calculate_average_raises_for_empty_input(self):
        with pytest.raises(ValueError, match="empty"):
            calculate_average([])


class TestStrings:
    """Tests for string behavior and normalization."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False
        assert is_even(-2) is True

    def test_is_palindrome(self):
        assert is_palindrome("racecar") is True
        assert is_palindrome("A man, a plan, a canal: Panama") is True
        assert is_palindrome("hello") is False

    def test_normalize_text(self):
        assert normalize_text("  Hello World  ") == "hello world"
        assert normalize_text("PYTEST") == "pytest"


class TestRegression:
    """Regression checks to protect common edge cases."""

    def test_process_batch_handles_mixed_values(self):
        assert process_batch([1, 2, 3, 4]) == [2, 4, 6, 8]
        assert process_batch([]) == []

    def test_reverse_string_round_trip(self):
        sample = "performance testing"
        assert reverse_string(reverse_string(sample)) == sample


class TestPerformanceSmoke:
    """Lightweight performance smoke tests to simulate load testing."""

    def test_process_batch_load_smoke(self):
        data = list(range(10000))
        start = time.perf_counter()
        result = process_batch(data)
        elapsed = time.perf_counter() - start

        assert len(result) == len(data)
        assert result[0] == 0
        assert result[-1] == 19998
        assert elapsed < 1.0

    def test_repeated_adds_under_load(self):
        start = time.perf_counter()
        total = 0
        for i in range(100000):
            total = add(total, 1)
        elapsed = time.perf_counter() - start

        assert total == 100000
        assert elapsed < 1.0
