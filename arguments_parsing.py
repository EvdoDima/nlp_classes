import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--src-texts", required=True) #corpus path
parser.add_argument("--text-encoding") #
parser.add_argument("--word-type", choices=["surface_all", "surface_no_pm", "stem","suffix_X"])
parser.add_argument("-n", type=int) #n-grams
parser.add_argument("--laplace", action="store_true")
parser.add_argument("--good-turing", action="store_true")
parser.add_argument("--unknown-word-freq", type=int)
parser.add_argument("-o", required=True)
parsed = parser.parse_args()

print parsed.src_texts
