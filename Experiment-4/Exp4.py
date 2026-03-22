n = int(input("Enter the no of words: "))

lis = []

for i in range(n):
    s = input("Enter the string: ")
    lis.append(s)


# Bigrams
bigrams = []

for i in range(len(lis)-1):
    bigrams.append((lis[i],lis[i+1]))

# Unigram Frequency
uni = {}

for i in lis:
    if i in uni:
        uni[i]+=1
    else:
        uni[i] = 1

# Bigram Frequency 
bi = {}

for i in bigrams:
    if i in bi:
        bi[i]+=1
    else:
        bi[i] = 1

# Vocabulary Size
v = len(uni)



print("Bigram Probabilites: ")
for b in bigrams:
    w1 = b[0]

    if w1 in uni:
        prob = (bi[b] + 1) / (uni[w1] + v)
        print(b,"=",prob)
    else:
        print(b,"=0") 
