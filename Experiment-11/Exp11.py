import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser


g = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    Adj -> 'big' | 'small'
    V  -> 'chased' | 'sat'
""")

parser = RecursiveDescentParser(g)
sentence = "the big dog chased a cat".split()


print("Sentence: ",sentence)
print("\n Parse Trees\n")

for tree in parser.parse(sentence):
    print(tree)
