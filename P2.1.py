#The function = load_words
def load_words():
    count = 0
    words = open("gamewords.txt", "r")
    #This statment opens the text file "gamewords.txt" where are the words are stored.
    for i in words:
    #The for loop is use to find the number of items in the text file, by going through each item in the text.
    #The loop stops counting once the progam reaches the end of the text file.
        count = count + 1
    print("There are " + str(count) + " words")
    #This statment returns the total number of words in the text file.
    words.close()


    words = open("gamewords.txt", "r")
    list_of_words = words.read()
    #This statment creates a variable to store the contents of the text file.
    print(list_of_words)
    #This prints the words in the list.
    words.close()




load_words()
