# rule-basedintent detection

Intents = {
    "greeting": ["hello", "hi", "hlo", "hey"],
    "goodbye" : ["bye", "goodbye", "see you", "farewell"],
    "name": ["what is your name", "whats your name", "whats ur name"],
    "calculation": ["calculate", "what is", "whats", "how much is"]
}

def detect_intent(message):
    input = message.lower()
    for intent, patterns in Intents.items():
        for pattern in patterns:
            if pattern in input:
                return intent


print(detect_intent("hello"))
print(detect_intent("what is your name"))
print(detect_intent("bye"))
print(detect_intent("calculate 2 + 2"))