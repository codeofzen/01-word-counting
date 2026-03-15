# Word Count Project

A Python utility that counts words and paragraphs in a given string.

## Project Structure

- [word_count.py](word_count.py) — main module with `count_words` and `count_paragraphs` functions
- [tests/test_word_count.py](tests/test_word_count.py) — pytest test suite
- [Makefile](Makefile) — `run` and `test` targets using Python 3.11

## Running

```bash
make run ARGS="your string here"
# or directly:
python3.11 word_count.py "your string here"
```

## Testing

Always run tests before committing. Tests must pass before any commit.

```bash
make test
# or directly:
python3.11 -m pytest tests/
```

## Key Behaviors

- `count_words(text)` — splits on whitespace (handles multiple spaces, tabs, newlines)
- `count_paragraphs(text)` — splits on `\n`; returns 0 for empty/whitespace-only input

## Python Version

Pinned to Python 3.11.9 via `.python-version`.
