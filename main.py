import json
from pathlib import Path

KNOWLEDGE_FILE = Path(__file__).with_name("knowledge.json")

def load_knowledge():
    try:
        with KNOWLEDGE_FILE.open("r", encoding="utf-8") as file:
            knowledge = json.load(file)

        if not isinstance(knowledge, dict):
            raise ValueError("Knowledge file must contain a JSON object.")

        return knowledge

    except FileNotFoundError:
        print("Error: knowledge.json was not found.")
        return {}

    except json.JSONDecodeError:
        print("Error: knowledge.json contains invalid JSON.")
        return {}

    except OSError as error:
        print(f"Error reading knowledge file: {error}")
        return {}

    except ValueError as error:
        print(f"Error in knowledge file: {error}")
        return {}

def get_response(user_message, knowledge):
    user_message = user_message.lower().strip()

    if user_message in knowledge:
        return knowledge[user_message]

    if "hello" in user_message or "hi" in user_message:
        return knowledge["hello"]

    if "python" in user_message:
        return knowledge["what is python"]

    return "Sorry, I don't understand that yet."


def chat():
    knowledge = load_knowledge()

    print("Welcome to PyBot!")
    print("Ask me about Python, machine learning, or AI.")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("You: ").strip()

        response = get_response(user_message, knowledge)
        print("PyBot:", response)

        if user_message.lower() == "bye":
            break


if __name__ == "__main__":
    chat()