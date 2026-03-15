PYTHON = python3.11

.PHONY: run test

run:
	$(PYTHON) word_count.py $(ARGS)

test:
	$(PYTHON) -m pytest tests/
