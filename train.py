from nltk.model import NgramModel
import nltk
import os, dill, pickle

text = ""
with open (os.getcwd() + "/input/1.txt", "r") as file:
	text = file.read()

# print(text)

lm = NgramModel(3, nltk.word_tokenize(text))
pickle.dump(lm, open("out.txt", "wb"))