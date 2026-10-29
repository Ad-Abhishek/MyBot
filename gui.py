import tkinter as tk
from tkinter import scrolledtext

from main import get_response, load_knowledge


class MyBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MyBot - Python Chatbot")
        self.root.geometry("700x600")
        self.root.minsize(500, 400)

        # Load chatbot knowledge once at startup.
        self.knowledge = load_knowledge()

        # Configure the main window.
        self.root.configure(bg="#f4f6f9")

        # Build the interface.
        self.create_header()
        self.create_chat_area()
        self.create_input_area()

        # Display the initial message.
        self.display_message(
            "MyBot",
            "Hello! I'm MyBot. Ask me about Python, machine learning, or AI."
        )

        # Focus the input field.
        self.message_entry.focus_set()

    def create_header(self):
        """Create the application header."""

        header = tk.Frame(
            self.root,
            bg="#243447",
            height=70
        )
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="MyBot",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#243447"
        )
        title.pack(side=tk.LEFT, padx=20, pady=15)

        subtitle = tk.Label(
            header,
            text="By Lunar Husky",
            font=("Arial", 10),
            fg="#dce6f1",
            bg="#243447"
        )
        subtitle.pack(side=tk.LEFT, pady=20)

        clear_button = tk.Button(
            header,
            text="Clear Chat",
            command=self.clear_chat,
            bg="#ffffff",
            fg="#243447",
            relief=tk.FLAT,
            padx=10,
            pady=5,
            cursor="hand2"
        )
        clear_button.pack(side=tk.RIGHT, padx=20)

    def create_chat_area(self):
        """Create the conversation display."""

        chat_frame = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )
        chat_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=15,
            pady=15
        )

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="white",
            fg="#243447",
            relief=tk.FLAT,
            padx=12,
            pady=12,
            state=tk.DISABLED
        )
        self.chat_area.pack(
            fill=tk.BOTH,
            expand=True
        )

        # Style the sender names.
        self.chat_area.tag_configure(
            "user",
            foreground="#1565c0",
            font=("Arial", 11, "bold")
        )

        self.chat_area.tag_configure(
            "bot",
            foreground="#16803c",
            font=("Arial", 11, "bold")
        )

        self.chat_area.tag_configure(
            "message",
            foreground="#243447",
            font=("Arial", 11)
        )

    def create_input_area(self):
        """Create the message input and send button."""

        input_frame = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )
        input_frame.pack(
            fill=tk.X,
            padx=15,
            pady=(0, 15)
        )

        self.message_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            relief=tk.FLAT,
            bg="white"
        )
        self.message_entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=10,
            padx=(0, 10)
        )

        self.message_entry.bind(
            "<Return>",
            self.handle_enter
        )

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 11, "bold"),
            bg="#1565c0",
            fg="white",
            activebackground="#0d47a1",
            activeforeground="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.send_button.pack(side=tk.RIGHT)

    def display_message(self, sender, message):
        """Display a message in the conversation."""

        self.chat_area.configure(state=tk.NORMAL)

        if sender == "You":
            tag = "user"
        else:
            tag = "bot"

        self.chat_area.insert(
            tk.END,
            f"{sender}: ",
            tag
        )

        self.chat_area.insert(
            tk.END,
            f"{message}\n\n",
            "message"
        )

        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def send_message(self):
        """Process the user's message and display the response."""

        user_message = self.message_entry.get().strip()

        if not user_message:
            return

        # Display the user's message.
        self.display_message("You", user_message)

        # Clear the input field.
        self.message_entry.delete(0, tk.END)

        # Use the existing NLP engine.
        response = get_response(
            user_message,
            self.knowledge
        )

        # Display the chatbot's response.
        self.display_message("MyBot", response)

    def handle_enter(self, event):
        """Send the message when Enter is pressed."""

        self.send_message()

        # Prevent the default event behavior.
        return "break"

    def clear_chat(self):
        """Clear the displayed conversation."""

        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.configure(state=tk.DISABLED)

        self.display_message(
            "MyBot",
            "Chat cleared. How can I help you?"
        )

        self.message_entry.focus_set()


def main():
    root = tk.Tk()

    app = MyBotGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()