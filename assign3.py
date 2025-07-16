contractions = {"ain't" : "am not" , "aren't" : "are not" , "can't" : "cannot" , "can't've" : "cannot have" , "cause" : "because" , 
                "could've" : "could have" , "couldn't" : "could not" , "couldn't've" : "could not have" , "didn't" : "did not" , "does't" : "does not" , "don't" : "do not"}
text = "i don't agree with this"

for word in text.split():
    if word.lower in contractions:
        text = text.replace(word,contractions[word.lower()])
    print(text)

