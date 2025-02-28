sentence= input ("Enter a sentence: ")
words= sentence.split ()
print (words)

word_dict = {}
for word in words:
    word_dict [word]= word_dict.get (word, 0)+1
print (word_dict)

def word_dictf (sentence):
    words= sentence.split ()

    word_dictf={}
    for word in words:
        word_dictf [word]= word_dictf.get (word, 0)+1
    return (word_dictf)

result=word_dictf ("A B B N N N M M M M N  B BB B B B" )
print (result)