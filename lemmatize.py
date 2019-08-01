import nltk
from nltk.stem import WordNetLemmatizer
document = "I saw your face I see your faces"
##create list of pos
tokens = nltk.word_tokenize(document)
tokens_with_pos = nltk.pos_tag(tokens)
print "tokens and their pos tag"
print tokens_with_pos
pos_list = []
for word,pos in tokens_with_pos:
    pos_list.append(pos)

##create list of lemmas
wnl = WordNetLemmatizer()
lemmas = []
lemma_string = ""
for token in tokens:
    lemma = wnl.lemmatize(token)
    lemmas.append(lemma)
    lemma_string += " "+lemma

##zip list of pos and list of lemmas
lemma_pos = zip(lemmas,pos_list)
##turn list into a set to remove duplicates
lemma_pos_set = set(lemma_pos)

##create freq dist of lemmas
fdist = nltk.FreqDist()
for word in nltk.word_tokenize(lemma_string):
    #word.lower turns the words to lowercase
    fdist[word.lower()] += 1

#create list for lemma pos and frequency
lemma_pos_freq = []

#insert lemma, pos and frequency of lowercase lemma to list
for lemma,pos in lemma_pos_set:
    lemma_pos_freq.append((lemma,pos,fdist[lemma.lower()]))

print "lemmas with pos tags and lemma frequency"
print lemma_pos_freq