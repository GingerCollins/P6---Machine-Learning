import nltk
from nltk.corpus import stopwords
#nltk.download()
sw = stopwords.words("english")

print sw[0]
print sw[10]
print "number of stop words:", len(sw)