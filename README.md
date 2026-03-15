# Word Count

Counts the number of words in a given string.

## Usage

```bash
python word_count.py "your string here"
```

## Example

```bash
$ python word_count.py "hello world foo"
Words: 3
Paragraphs: 1
```

```bash
$ python word_count.py $'hello world\nfoo bar\nbaz'
Words: 5
Paragraphs: 3
```

## Running Tests

Requires [pytest](https://pytest.org). Install it with:

```bash
pip install pytest
```

Then run:

```bash
pytest tests/
```
