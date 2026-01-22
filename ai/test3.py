

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("bye", "goodbye"),
    ("goodbye", "goodbye"),
    ("see you", "goodbye"),
    ("what is your name", "name"),
    ("whats your name", "name"),
    ("whats ur name", "name"),
    ("calculate", "calculation"),
    ("what is", "calculation"),
    ("whats", "calculation"),
    ("how much is", "calculation")
]

texts = [text for text, label in training_data]
labels =[label for text, label in training_data]

vecotrizer = TfidfVectorizer()
x = vecotrizer.fit_transform(texts)

model = LogisticRegression()
model.fit(x, labels)

def detect_intent(text):
    vector = vecotrizer.transform([text])
    intent = model.predict(vector)[0]
    return intent


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    intent = detect_intent(user_input)
    print(f"Bot: {intent}")