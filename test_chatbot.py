import unittest

from main import (
    find_best_intent,
    get_response,
    load_knowledge,
    normalize_text,
    tokenize,
)


class TestNaturalLanguageProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.knowledge = load_knowledge()

    def test_text_normalization(self):
        self.assertEqual(
            normalize_text("  HELLO!!!  "),
            "hello"
        )

    def test_tokenization(self):
        self.assertEqual(
            tokenize("What is Python?"),
            ["what", "is", "python"]
        )

    def test_exact_intent_match(self):
        self.assertEqual(
            find_best_intent("hello", self.knowledge),
            "greeting"
        )

    def test_case_insensitive_match(self):
        self.assertEqual(
            find_best_intent("HELLO", self.knowledge),
            "greeting"
        )

    def test_punctuation_handling(self):
        self.assertEqual(
            find_best_intent("Hello!!!", self.knowledge),
            "greeting"
        )

    def test_different_phrasing(self):
        self.assertEqual(
            find_best_intent("explain python", self.knowledge),
            "python"
        )

    def test_fuzzy_matching(self):
        self.assertEqual(
            find_best_intent("helo", self.knowledge),
            "greeting"
        )

    def test_unknown_message(self):
        self.assertIsNone(
            find_best_intent(
                "What is the weather on Mars today?",
                self.knowledge
            )
        )

    def test_response_generation(self):
        response = get_response("what is python", self.knowledge)

        self.assertIn(
            response,
            self.knowledge["python"]["responses"]
        )


if __name__ == "__main__":
    unittest.main()