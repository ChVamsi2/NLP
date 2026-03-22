from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

lis = []
n = int(input("Enter the no of words: "))
for i in range(n):
    s = input("Enter the string: ")
    lis.append(s)


# Stemming
ps = PorterStemmer()

for i in lis:
    print(ps.stem(i))



# Lemmatization
l = WordNetLemmatizer()
print(l.lemmatize("foods"))
