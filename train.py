#!/usr/bin/python
# -*- coding: utf8 -*-

from nltk.model import NgramModel
import nltk
import string
import os, dill
import Stemmer
import argparse
from nltk.probability import FreqDist
from nltk.corpus import brown
from nltk.probability import LaplaceProbDist, SimpleGoodTuringProbDist

parser = argparse.ArgumentParser()
parser.add_argument("--src-texts", required=True) #corpus path
parser.add_argument("--text-encoding") #
parser.add_argument("--word-type")
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
		inp = file.read()
		if parsed.text_encoding:
			inp = inp.decode(parsed.text_encoding)

		if filename != ".DS_Store":
			if parsed.word_type == "stem":
				stemmer = Stemmer.Stemmer('russian')
				words += stemmer.stemWords([inp])
			elif parsed.word_type == "surface_all":
				words += nltk.word_tokenize(inp)
			elif parsed.word_type == "surface_no_pm" or parsed.word_type[:7] == "suffix_":
				inp = inp.translate(None, string.punctuation)
				words += nltk.word_tokenize(inp)
			else:
				words += nltk.word_tokenize(inp)
			

if parsed.word_type[:7] == "suffix_":
	l = int(parsed.word_type.split("_")[1])
	words = [x[-l:] for x in words]

if parsed.unknown_word_freq:
	unknown_words = []
	# print "Removing unknown words"
	fq = FreqDist(words)
	for w, count in fq.iteritems():
		if count < parsed.unknown_word_freq:
			unknown_words += w

	words[:] = [x if x not in unknown_words else "<UNK>" for x in words]

lm = NgramModel(n, words, estimator=estimator)
outf = open(output, "wb")
dill.dump(lm, outf ,protocol= 2)
outf.close()
