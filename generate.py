#!/usr/bin/python
# -*- coding: utf8 -*-

from nltk.model import NgramModel
import nltk
import string
import argparse, os, dill

parser = argparse.ArgumentParser()
parser.add_argument("--lm", required=True) #lm path
parsed = parser.parse_args()

with open("/Users/rinat/dev/nlp_classes/output.pk", 'rb') as f:
	lm = dill.load(f)

	print (lm)
