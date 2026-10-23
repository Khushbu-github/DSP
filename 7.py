#Experiment 7 — Phishing Website Detection
#Question
#Write a Python program using Machine Learning to classify a URL as phishing or legitimate.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

urls = [
    "http://free-gift.com",
    "http://verify-account.com",
    "https://google.com",
    "https://github.com"
]

labels = [1, 1, 0, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)

model = LogisticRegression()
model.fit(X, labels)

url = input("Enter URL: ")

result = model.predict(vectorizer.transform([url]))

if result[0] == 1:
    print("PHISHING")
else:
    print("LEGITIMATE")