import unittest

from main import get_response


class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.knowledge = {
            "hello": "Hello! How can I help you?",
            "what is python": "Python is a programming language.",
            "bye": "Goodbye! Have a great day!"
        }

    def test_exact_match(self):
        response = get_response("hello", self.knowledge)

        self.assertEqual(
            response,
            "Hello! How can I help you?"
        )

    def test_case_insensitive_match(self):
        response = get_response("HELLO", self.knowledge)

        self.assertEqual(
            response,
            "Hello! How can I help you?"
        )

    def test_whitespace_handling(self):
        response = get_response("  hello  ", self.knowledge)

        self.assertEqual(
            response,
            "Hello! How can I help you?"
        )

    def test_unknown_message(self):
        response = get_response("tell me a joke", self.knowledge)

        self.assertEqual(
            response,
            "Sorry, I don't understand that yet."
        )


if __name__ == "__main__":
    unittest.main()