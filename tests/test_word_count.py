import pytest
from word_count import count_words, count_paragraphs


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


def test_paragraphs_single():
    assert count_paragraphs("hello world") == 1

def test_paragraphs_multiple():
    assert count_paragraphs("hello\nworld\nfoo") == 3

def test_paragraphs_empty():
    assert count_paragraphs("") == 0

def test_paragraphs_two():
    assert count_paragraphs("first line\nsecond line") == 2
