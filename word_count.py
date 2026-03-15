import sys

def count_words(text):
    return len(text.split())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py \"<string>\"")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    print(count_words(text))
