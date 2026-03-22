from nltk import ngrams

s = input("Enter the string: ")
value = int(input("Enter the value: "))

words = s.split()

res = ngrams(words,value)

for i in res:
    print(i)
