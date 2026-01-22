# ml based intent detection

# converts text to numbers and ml classifier learns patterns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# training data

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

# seperate text and labels

texts = [text for text, label in training_data]
labels = [label for text, label in training_data]

# convert text to numbers
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(texts)

# train ai model
model = LogisticRegression()
model.fit(x, labels)

# intent detection function
def detect_intent(text):
    vector = vectorizer.transform([text])
    intent = model.predict(vector)[0]
    return intent

# test the function
while True:
    user_input = input("You:")
    if user_input.lower() == "exit":
        break
    intent = detect_intent(user_input)
    print(f"Bot: {intent}")
