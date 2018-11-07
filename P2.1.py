words = open("words.txt", 'r')

def load_words(words):
    words.write("\n")
    words.close()



load_words(words)