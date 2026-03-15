.PHONY: run test

run:
	python word_count.py $(ARGS)

test:
	python3.11 -m pytest tests/
