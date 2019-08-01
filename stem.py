import nltk

document = "I saw your face I see your faces"
tokens = nltk.word_tokenize(document)
tokens_with_pos = nltk.pos_tag(tokens)

from nltk.stem.snowball import SnowballStemmer
for word in tokens:
    print "word: " + word
    stemmer = SnowballStemmer("english")
    stem = stemmer.stem(word);
    print "stem: " + stem
