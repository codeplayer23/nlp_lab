## Root word is wrong for accepting 

import nltk 
from nltk.stem import LancasterStemmer

lancaster_stem = LancasterStemmer()

print(lancaster_stem.stem("accepting"))
print(lancaster_stem.stem("heavier"))
print(lancaster_stem.stem("programming"))
