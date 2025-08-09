def respond_to_input(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm doing great, thank you!"
    elif user_input == "what's your name":
        return "I'm just a simple chatbot."
    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions."
    elif user_input == "tell me a joke":
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

print("Chatbot: Hello! Type 'bye' to end the chat.")

while True:
    user_input = input("You: ")
    reply = respond_to_input(user_input)
    print("Chatbot:", reply)

    if user_input.lower() == "bye":
        break
