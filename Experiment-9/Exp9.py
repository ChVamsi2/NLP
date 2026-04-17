from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    'Natural Language Processing is fun.',
    'Machine Learning is part of AI.',
    'NLP and Machine Learning is closely related.'
]

v = TfidfVectorizer()
x = v.fit_transform(documents)

print("Feature Names: ",v.get_feature_names_out())
print("TF-IDF Matrix: ")
print(x.toarray())
