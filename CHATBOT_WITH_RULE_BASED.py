import re

def chatbot():
    print("AI Chatbot: Hello! I'm an AI chatbot. You can ask me about Artificial Intelligence, technology, or just general questions.")
    print("Type 'bye' anytime to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("AI Chatbot: See you later! Have a great day ahead!")
            break

        elif re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
            print("AI Chatbot: Hello! I'm glad to chat with you. What do you want to know today?")

        elif re.search(r"your name", user_input):
            print("AI Chatbot: I'm a basic AI chatbot created using Python. You can call me AI Bot!")

        elif re.search(r"how are you", user_input):
            print("AI Chatbot: I'm always operational! Thanks for asking. What can I assist you with?")

        elif re.search(r"what is artificial intelligence", user_input):
            print("AI Chatbot: Artificial Intelligence is the simulation of human intelligence in computers. "
                  "It allows machines to learn, reason, and make decisions based on data.")

        elif re.search(r"who created you", user_input):
            print("AI Chatbot: I was created by a Python programmer as a simple AI project using rule-based logic.")

        elif re.search(r"what can you do", user_input):
            print("AI Chatbot: I can answer basic questions, explain concepts, and hold simple conversations. "
                  "I work using if-else rules and pattern matching!")

        elif re.search(r"\bthanks\b|\bthank you\b", user_input):
            print("AI Chatbot: Anytime! Let me know if you have more questions.")

        # Keyword-based guess (if not exact match)
        elif "ai" in user_input or "machine" in user_input:
            print("AI Chatbot: Sounds like you're interested in AI or machines. I can help with that! Ask me something specific about AI.")

        elif "python" in user_input:
            print("AI Chatbot: Python is a powerful programming language that's great for AI and data science!")

        elif "technology" in user_input:
            print("AI Chatbot: Technology is evolving rapidly, especially in fields like AI, robotics, and data science.")

        # Default fallback
        else:
            print("AI Chatbot: That's an interesting question! I'm still learning, so I might not have a perfect answer. "
                  "Try asking about AI, Python, or general tech topics!")

# Run the chatbot
chatbot()