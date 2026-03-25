#porterstemmer
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer
porter = PorterStemmer()
words = ['Connects','Connecting','Connections','Connected','Connection','Connectings','Connect']
print("Porter Stemmer:")
for word in words:
   print(word,"--->",porter.stem(word))

#snowballstemmer
snowball = SnowballStemmer(language='english')
words = ['generous','generate','generously','generation']
print("\nSnowball Stemmer:")
for word in words:
    print(word,"--->",snowball.stem(word))

#LancasterStemmer
lancaster = LancasterStemmer()
words = ['eating','eats','eaten','puts','putting']
print("\nLancaster Stemmer:")
for word in words:
    print(word,"--->",lancaster.stem(word))

#RegexpStemmer
regexp = RegexpStemmer('ing$|s$|e$|able$', min=4)
words = ['mass','was','bee','computer','advisable']
print("\n Regexp Stemmer:")
for word in words:
    print(word,"--->",regexp.stem(word))
