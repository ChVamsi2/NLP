import nltk 
from nltk.stem import PorterStemmer,LancasterStemmer,RegexpStemmer,SnowballStemmer 


n = int(input("Enter no of inputs: "))

words = []
print("Enter the words: ")
for i in range(n):
    s = input()
    words.append(s)


p = PorterStemmer()
l = LancasterStemmer()
s = SnowballStemmer('english')
r = RegexpStemmer('ing$|e$|s$|able$',min=4)


print("Word\t\tPorter\t\tLancaster\tSnowball")

for i in words:
    print(f"{p.stem(i)}\t\t{l.stem(i)}\t\t{s.stem(i)}\t\t{r.stem(i)}")
