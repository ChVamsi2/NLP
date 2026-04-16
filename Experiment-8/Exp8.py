import nltk
from nltk.corpus import treebank 
from nltk.tag import hmm 

tagged_sentences = treebank.tagged_sents()
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(tagged_sentences[:30000])

s = input("Enter the sentence: ").split()

tags = hmm_tagger.tag(s)

print("Sentence: ",s)
print("POS tags: ",tags)
