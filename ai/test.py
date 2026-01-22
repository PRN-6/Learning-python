

def chat():
    print("Bot: Hello! How can I help you today? type 'exit' to quit")
    while True:
        user_input = input("You:").lower()
        if user_input == "exit":
            break
        if user_input == "hello":
            print("Bot: Hello! How can I help you today?")
        elif user_input == "how are you":
            print("Bot: Iam fine, how can I help you today?")
        else:
            print("Bot: I dont understand")


chat()
