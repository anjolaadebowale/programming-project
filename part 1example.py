


find =  ['a','n','j','o','l','a']
empty = ['*','*','*','*','*','*']
tries= 10


#you didn't define count in 'is_word_guessed(secret_word,letters_guessed):' btw
def hangman():
    guess = 10
    for i in range (tries ):

        if str(empty) == str(find):
            break

        user= (input("Enter a letter: "))
        guess = guess - 1
        print("you have  "+ str(guess)+ "  guesses left")

        if user == find[0]:
            empty[0]='a'
            empty[5]='a'
            print ("that was correct  " + ','.join(empty))


        elif user == find[1]:
            empty[1]='n'
            print("that was correct  " + ','.join(empty))

        elif user == find[2]:
            empty[2]='j'
            print("that was correct  " + ','.join(empty))


        elif user == find[3]:
            empty[3]='o'
            print("that was correct  " + ','.join(empty))


        elif user == find[4]:
            empty[4]='l'
            print("that was correct  " + ','.join(empty))


        elif user != find[0:]:
            print("that letter is wrong! Try again")




    if find  ==  empty:
        print ("You completed the word!  " + ','.join(empty))

    else:
        print("you failed to find the word")
        print("you found"+','.join(empty))


#it's really simple so I didn't bother adding comments

hangman()#i tried it out at a basic level but I'll upload my other one with the function names and stuff tommorow if i can actually get it to work
