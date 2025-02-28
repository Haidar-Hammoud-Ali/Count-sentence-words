sentence= input ("Enter a sentence: ")
words= sentence.split ()
print (words)

word_dict = {}
for word in words:
    word_dict [word]= word_dict.get (word, 0)+1
print (word_dict)