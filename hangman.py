from random import choice
from display import hangedman

player_score = 0
computer_score = 0

def start():
    print("LET THE GAME BEGIN")
    while game():
        pass
    scores()

def game():
    dictionary = ["linux", "kernal", "networks", "python"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * "_"
    tries = 6
    letters_tried = ""
    wrong_letters = 0
    global computer_score, player_score

    while (wrong_letters != tries) and (clue != word):
        letter=guess_letter()

        if len(letter)==1 and letter.isalpha():

            if letters_tried.find(letter)+1:
                print("This letter has already been chosen")
            else:
                letters_tried += letter
                first_index=word.find(letter)

                if first_index == -1:
                    wrong_letters+=1
                    print("NOPE...HA!")
                else:
                    print(f"Congratulations, {letter} is correct")

                    for i in range(word_length):

                        if letter == word[i]:
                            clue = clue[:i] + letter + clue[i+1:]
        else:
            print("Choose something else please")

        if(wrong_letters) > 0:
            hangedman(wrong_letters-1)

        print(clue)
        print(f"Guesses: {letters_tried}")

        if wrong_letters == tries:
            print("GAME OVER!")
            print(f"The word was: {word}")
            computer_score += 1
            break
        if clue == word:
            print("YOU WIN!")
            print(f"{word} was the word! Well done")
            player_score += 1
            break
    return play_again()

def guess_letter():
    print("")
    letter = input("Take a guess, insert a letter: ").strip().lower()
    print("")
    return letter

def play_again():
    print("")
    answer = input("Play again? Y/N: ")
    if answer in("y", "Y", "Yes", "yes", "Of Course!"):
        return True
    else:
        print("Thanks for playing - Until next time...")
        return False

def scores():
    global player_score, computer_score
    print("SCORES")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

start()