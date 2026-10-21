from texttools import (
    count_words,
    count_characters,
    reverse_text,
    is_palindrome,
    capitalize_words
)


def test_count_words():
    assert count_words("Hello world") == 2


def test_count_characters():
    assert count_characters("Hello") == 5


def test_reverse_text():
    assert reverse_text("hello") == "olleh"


def test_is_palindrome():
    assert is_palindrome("madam") is True


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"