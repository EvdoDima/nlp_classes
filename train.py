from nltk.model import NgramModel
import nltk
<<<<<<< HEAD
import os, pickle
=======
import os, dill, pickle
>>>>>>> f4d6cfffffe2fcd6ee1cb7406189106ca01d75f3

text = ""
with open (os.getcwd() + "/input/1.txt", "r") as file:
	text = file.read()

# print(text)

lm = NgramModel(3, nltk.word_tokenize(text))
<<<<<<< HEAD
pickle.dump(lm, open("out.txt", "wb"),protocol=pickle.HIGHEST_PROTOCOL)
=======
pickle.dump(lm, open("out.txt", "wb"))
>>>>>>> f4d6cfffffe2fcd6ee1cb7406189106ca01d75f3
