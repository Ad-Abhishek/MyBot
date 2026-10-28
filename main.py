import json
import random
import re
from pathlib import Path

from rapidfuzz import fuzz, process


KNOWLEDGE_FILE = Path(__file__).with_name("knowledge.json")

FUZZY_MATCH_THRESHOLD = 75


def load_knowledge():
    """Load chatbot intents and responses from a JSON file."""

    try:
        with KNOWLEDGE_FILE.open("r", encoding="utf-8") as file:
            knowledge = json.load(file)

        if not isinstance(knowledge, dict):
            raise ValueError("Knowledge must be a JSON object.")

        for intent, data in knowledge.items():
            if not isinstance(data, dict):
                raise ValueError(f"Invalid structure for intent: {intent}")

            if not isinstance(data.get("patterns"), list):
                raise ValueError(f"Missing patterns for intent: {intent}")

            if not isinstance(data.get("responses"), list):
                raise ValueError(f"Missing responses for intent: {intent}")

            if not data["patterns"] or not data["responses"]:
                raise ValueError(f"Empty patterns or responses: {intent}")

        return knowledge

    except (OSError, json.JSONDecodeError, ValueError) as error:
        raise RuntimeError(
            f"Could not load chatbot knowledge: {error}"
        ) from error


def normalize_text(text):
    """Normalize text before matching."""

    text = text.lower().strip()

    # Remove punctuation while preserving word boundaries.
    text = re.sub(r"[^\w\s]", "", text)

    # Replace repeated whitespace with a single space.
    text = re.sub(r"\s+", " ", text)

    return text


def tokenize(text):
    """Split normalized text into words."""

    return normalize_text(text).split()


def find_best_intent(user_message, knowledge):
    """Find the intent that best matches the user's message."""

    normalized_message = normalize_text(user_message)

    if not normalized_message:
        return None

    normalized_patterns = {}

    for intent, data in knowledge.items():
        for pattern in data["patterns"]:
            normalized_patterns[normalize_text(pattern)] = intent

    # First, try an exact match.
    if normalized_message in normalized_patterns:
        return normalized_patterns[normalized_message]

    # Then, try to find a phrase embedded in the message.
    message_tokens = set(tokenize(normalized_message))

    for pattern, intent in normalized_patterns.items():
        pattern_tokens = set(tokenize(pattern))

        if pattern_tokens and pattern_tokens.issubset(message_tokens):
            return intent

    # Finally, try fuzzy matching.
    best_match = process.extractOne(
        normalized_message,
        normalized_patterns.keys(),
        scorer=fuzz.ratio,
        score_cutoff=FUZZY_MATCH_THRESHOLD
    )

    if best_match:
        matched_pattern = best_match[0]
        return normalized_patterns[matched_pattern]

    return None


def get_response(user_message, knowledge):
    """Generate a response based on the detected intent."""

    intent = find_best_intent(user_message, knowledge)

    if intent is None:
        return (
            "I'm not sure I understand. "
            "Try asking me about Python, machine learning, or AI."
        )

    responses = knowledge[intent]["responses"]

    return random.choice(responses)


def chat():
    """Run the terminal chatbot."""

    knowledge = load_knowledge()

    print("Welcome to PyBot!")
    print("Ask me about Python, machine learning, or AI.")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("You: ")

        intent = find_best_intent(user_message, knowledge)

        if intent == "farewell":
            print("PyBot:", get_response(user_message, knowledge))
            break

        print("PyBot:", get_response(user_message, knowledge))


if __name__ == "__main__":
    chat()