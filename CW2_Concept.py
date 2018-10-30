letters_guessed = []
# The list, letters_guessed, containing the user's guesses is empty because the game has not started.
secret_word = "Corporation"
# The secret word, "Corporation", is a string assigned to a constant variable called secret_word. This is Player 1's secret word.
for i in range(0,len(secret_word)):
    letters_guessed.append("_")
# this FOR statement repeats adding "_" as a character to the letters_guessed list. The number of times it does so is the same number as the length of the variable secret_word.
letter_guessed = ""
# The variable letter_guessed is an empty string because the game has not started. In other words, the user has not made any guesses.
count = 11
# Because the game has not started, no letters have been guessed. Hence, the number of guesses is 11 which is stored in a variable, count.
rule = True
# The following WHILE statement uses count to simulate guesses, hence the need to initialize count = 11. This begins the Hangman game.
while count != 0:
# In order for the game to end, the variable count must equal 0.
    if count == 1:
        print("You have",str(count),"guess left to determine what my secret word is.")
# This IF statement checks if there is 1 guess left. If so, the message changes to reflect this. It does not make sense saying "1 guesses".
    else:
        print("You have",str(count),"guesses left to determine what my secret word is.")
# Displays an output telling the user how many guesses they have left to decipher the secret word.
    letter_guessed = input("Guess a letter in the word: ")
# The variable letter_guessed simulates the user's guess by taking in a one letter input.
    if len(letter_guessed) != 1:
        rule = False
# If the user tries to enter more than one letter at a time, they will be presented with a message and asked to re-input a letter. It will not result in the user losing a guess.
    while rule == False:
        letter_guessed = input("You can only guess one letter at a time. Guess a letter in the word: ")
        if len(letter_guessed) == 1:
            rule = True
        else:
            rule = False
# If the user does input 1 letter, then the WHILE statement ends and the game continues. Otherwise, the WHILE statement continues.
    for j in range(0,len(secret_word)):
        if letter_guessed == secret_word[j]:
            letters_guessed[j] = letter_guessed
# Replaces the current "_" with the user's guess in the letters_guessed list at the current index.
        else:
            continue
    count -= 1
# This FOR statement replaces every "_" in the letters_guessed list with the user's guess if said guess is found in the secret word.
    if "".join(letters_guessed) == secret_word and count >= 0:
        print("You Win! The word was",secret_word)
# This IF statement checks if the user successfully guesses all letters in the secret word. If this happens, the game ends and the player is given the message "You Win!"
        break
    elif "".join(letters_guessed) != secret_word and count > 0:
        print("So far, the partially solved word is:","".join(letters_guessed))
# This ELIF statement checks if the user has not successfully guessed all the letters in the secret word but still has guesses left. The partially solved word is displayed.
    else:
        print("You Lose! The word was",secret_word)
# If the player has ran out of guesses and not guessed the secret word, the game ends and the player is given the message "You Lose."
