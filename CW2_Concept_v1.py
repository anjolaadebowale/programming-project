letters_guessed = []
secret_word = "Corporation"
for i in range(0,len(secret_word)):
    letters_guessed.append("_")
letter_guessed = ""
count = 11
while count != 0:
    print("You have",str(count),"guesses left to determine what my secret word is.")
    letter_guessed = input("Guess a letter in the word: ")
    for j in range(0,len(secret_word)):
        if letter_guessed == secret_word[j]:
            letters_guessed[j] = letter_guessed
        else:
            continue
    if "".join(letters_guessed) == secret_word and count >= 0:
        print("You Win! The word was",secret_word)
        break
    elif "".join(letters_guessed) != secret_word and count >= 0:
        print("The partially guessed word is:","".join(letters_guessed))
    else:
        print("You Lose!")
        break
    count -= 1
