"""Encrypt text with a substitution cipher, and crack it back using English statistics.

Usage:
    python crack.py demo                    # encrypt the sample text with a random key, then crack it
    python crack.py encrypt <file>          # encrypt a file with a random key
    python crack.py crack <file>            # crack a substitution cipher
    python crack.py crack <file> --caesar   # crack a Caesar (shift) cipher
"""
import argparse
import os
import random

from cipher import (break_ceaser_code, break_code, break_code_with_words,
                    encrypt, random_code)
from language_dict import compute_letters_frequencies, compute_words_frequencies

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "data", "english_corpus.txt")
SAMPLE = os.path.join(HERE, "data", "sample_text.txt")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def english_statistics():
    corpus = read(CORPUS)
    return compute_letters_frequencies(corpus), compute_words_frequencies(corpus)


def accuracy(guess, original):
    """Share of letters in the original text that the guess got right."""
    pairs = [(g, o) for g, o in zip(guess, original) if o.isalpha()]
    return sum(g == o for g, o in pairs) / len(pairs)


def show(title, text, chars=400):
    print(f"\n=== {title} ===\n{text[:chars].rstrip()}\n...")


def demo(seed=None):
    plain = read(SAMPLE).lower()
    random.seed(seed)
    secret = encrypt(plain, random_code())
    letters, words = english_statistics()

    step1, _ = break_code(secret, letters)
    step2, _ = break_code_with_words(secret, letters, words)

    show("Encrypted", secret)
    show(f"Step 1 - letter frequencies only ({accuracy(step1, plain):.0%} of letters right)", step1)
    show(f"Step 2 - improved with English words ({accuracy(step2, plain):.0%} of letters right)", step2)


def main():
    parser = argparse.ArgumentParser(description="Substitution cipher cracker.")
    sub = parser.add_subparsers(dest="command", required=True)
    d = sub.add_parser("demo", help="encrypt the sample text and crack it")
    d.add_argument("--seed", type=int, help="fix the random key")
    e = sub.add_parser("encrypt", help="encrypt a file with a random key")
    e.add_argument("file")
    c = sub.add_parser("crack", help="crack an encrypted file")
    c.add_argument("file")
    c.add_argument("--caesar", action="store_true", help="the text is a Caesar (shift) cipher")
    args = parser.parse_args()

    if args.command == "demo":
        demo(args.seed)
    elif args.command == "encrypt":
        print(encrypt(read(args.file).lower(), random_code()), end="")
    elif args.caesar:
        guess, shift = break_ceaser_code(read(args.file).lower(), english_statistics()[1])
        print(f"Shift: {shift}\n\n{guess}", end="")
    else:
        letters, words = english_statistics()
        guess, _ = break_code_with_words(read(args.file).lower(), letters, words)
        print(guess, end="")


if __name__ == "__main__":
    main()
