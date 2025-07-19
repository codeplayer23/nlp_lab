import nltk 
from nltk.stem import SnowballStemmer

snowball_stem = SnowballStemmer('english')

print(snowball_stem.stem("Running"))
print(snowball_stem.stem("Playing"))
print(snowball_stem.stem("Coding"))
print(snowball_stem.stem("Ate"))
