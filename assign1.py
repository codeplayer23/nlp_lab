from nltk.tokenize import sent_tokenize , word_tokenize
EXAMPLE_TEXT = "Hello Mr Smith , how are you doing today ? The weather is great , and python is awesome . The sky is pinkish-blue . You should'nt eat cardboard. Hello world."
print(sent_tokenize(EXAMPLE_TEXT))
print("\n")
print(word_tokenize(EXAMPLE_TEXT))
 