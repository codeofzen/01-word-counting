import sys

def count_words(text):
    return len(text.split())

def count_paragraphs(text):
    if not text.strip():
        return 0
    return len(text.split("\n"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py \"<string>\"")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    print(f"Words: {count_words(text)}")
    print(f"Paragraphs: {count_paragraphs(text)}")
