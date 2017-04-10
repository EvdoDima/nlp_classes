#!/usr/bin/python
# -*- coding: utf8 -*-

from nltk.model import NgramModel
import nltk
import os, dill, pickle
import argparse
from nltk.corpus import brown
from nltk.probability import LaplaceProbDist, SimpleGoodTuringProbDist

parser = argparse.ArgumentParser()
parser.add_argument("--src-texts", required=True) #corpus path
parser.add_argument("--text-encoding") #
parser.add_argument("--word-type", choices=["surface_all", "surface_no_pm", "stem","suffix_X"])
parser.add_argument("-n", type=int) #n-grams

group = parser.add_mutually_exclusive_group()
group.add_argument("--laplace", action="store_true")
group.add_argument("--good-turing", action="store_true")

parser.add_argument("--unknown-word-freq", type=int)
parser.add_argument("-o", required=True)
parsed = parser.parse_args()

estimator = None
if parsed.laplace:
	estimator = lambda fdist, bins: LaplaceProbDist(fdist)
elif parsed.good_turing:
	estimator = lambda fdist, bins: SimpleGoodTuringProbDist(fdist, bins=1e5)

words = []
directory = parsed.src_texts
n = parsed.n
output = parsed.o

for filename in os.listdir(directory):
	with open (directory+"/"+filename, "r") as file:
		if filename != ".DS_Store":
			# print(filename)
			words += nltk.word_tokenize(file.read())

# print words

lm = NgramModel(n, words, estimator=estimator)
# pickle.dump(lm, open(output, "wb"))

print lm.prob("Тора", ["И ПТИЦЫ ДА РАЗМНОЖАЮТСЯ НА ЗЕМЛЕ"])

print lm.prob("ЗЕМЛЕ", ["И ПТИЦЫ ДА РАЗМНОЖАЮТСЯ НА"])
