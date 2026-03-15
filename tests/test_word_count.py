import pytest
from word_count import count_words


def test_basic():
    assert count_words("hello world") == 2

def test_single_word():
    assert count_words("hello") == 1

def test_empty_string():
    assert count_words("") == 0

def test_multiple_spaces():
    assert count_words("hello   world") == 2

def test_leading_trailing_spaces():
    assert count_words("  hello world  ") == 2

def test_newlines():
    assert count_words("hello\nworld") == 2

def test_tabs():
    assert count_words("hello\tworld") == 2

def test_long_string():
    assert count_words("one two three four five") == 5
