def choose_secret_word():
    words = open("gamewords.txt", "r")
    #This opens the text file that contains the words
    count=0
    for i in words:
     #Use the for loop to find the total number of words, to use as the range when using "randrange".
     #Ensuring the random number can be matched to a word.
        count=count+1
    print(count)
    words.close()

    words = open("gamewords.txt", "r")
    import random
    randomnum = random.randrange(count)
    #This generates a random integer below the total number words.
    print(randomnum)
    secret_word=  words.readlines()
    #This statment allows for a specific line in the text file to be read rather than the whole file
    words.close()
    return (secret_word[randomnum])
     #This returns the word with the index of the radom number selected






secret_word=choose_secret_word()
#Assignes the word selected within the function to the variable (secret_word)
#This is outside the loop so it is a global variable rather than a local variable
print(secret_word)
