import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cipher import (break_ceaser_code, break_code_with_words, ceaser_code, decrypt,
                    encrypt, random_code, sort_dict_keys_by_value)
from language_dict import (compute_letters_frequencies, compute_words_frequencies,
                           dict_to_string, string_to_dict)
import crack


class LanguageDictTests(unittest.TestCase):
    def test_letter_frequencies(self):
        freq = compute_letters_frequencies("Hello, banana pack.")
        self.assertAlmostEqual(sum(freq.values()), 1)
        self.assertAlmostEqual(freq["a"], 4 / 15)

    def test_word_frequencies(self):
        freq = compute_words_frequencies("To be or not to be")
        self.assertAlmostEqual(freq["to"], 2 / 6)

    def test_string_round_trip(self):
        d = {"b": 0.1, "a": 0.4, "n": 0.2}
        self.assertEqual(string_to_dict(dict_to_string(d)), d)


class CipherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.letters, cls.words = crack.english_statistics()
        cls.plain = crack.read(crack.SAMPLE).lower()

    def test_encrypt_then_decrypt(self):
        code = random_code()
        self.assertEqual(decrypt(encrypt("hello world", code), code), "hello world")

    def test_sort_keeps_input_intact(self):
        d = {"a": 1, "b": 3, "c": 2}
        self.assertEqual(sort_dict_keys_by_value(d), ["b", "c", "a"])
        self.assertEqual(len(d), 3)

    def test_break_caesar(self):
        guess, shift = break_ceaser_code(encrypt(self.plain, ceaser_code(11)), self.words)
        self.assertEqual(guess, self.plain)
        self.assertEqual(shift, 11)

    def test_break_substitution(self):
        random.seed(1)
        guess, _ = break_code_with_words(encrypt(self.plain, random_code()), self.letters, self.words)
        self.assertEqual(guess, self.plain)


if __name__ == "__main__":
    unittest.main()
