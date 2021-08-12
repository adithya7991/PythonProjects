from words import words
import random as r
from hangman_visual import lives_visual_dict as v
'''
This is hangman game with custom rules and logic, It is all about picking a random word from words list and 
presenting to user with few letters missing. And the user should start guessing the word by filling in the letters.
No of guessess = 7. 
For each of guess miss, the hangman construction starts/increases.
For each of guess hit, the hangman construction decreases if it is not in initial state.
If player looses, he gets hanged.

'''

# Randomly picks a word from words list
generate = lambda word_list :  word_list[r.randint(0,len(words)-1)]

# Returns the list of indexes where letter occurs in original word where @ the same index in modified word it is "_"
occurance = lambda o_word, m_word, letter: [i for i in range(0, len(o_word)) if letter == o_word[i] and m_word[i] == "_" ]


# Core game logic
def play():    

    while True:

        print("WELCOME TO HANGMAN GAME!!")
        original_word = list(generate(words))        
        word_length = len(original_word)
        modified_word = []
        # To track whether player won/not         
        is_won = False
        # To track and display hanging visual
        hang_visual_tracker = 0

        # Logic for which letter positions in word are open for guessess
        # For even sized word length, even positions are hidden and odd positions for odd sized word
        if word_length%2 == 0:
            skip = True
        else:
            skip = False

        for i in original_word:
            if skip:
                skip = False
                modified_word.append(i)
                continue
            else:
                modified_word.append("_")
                skip = True

        # print(original_word)
        print("Your current word: {}".format("".join(modified_word)))        
        print("You are provided with 7 guessess to escape from hanging!")

        # 7 Guessess
        for gues_num in range(0,len(v)):

            guess = input(("Input your guess no. {} for the word: ").format(gues_num))

            if guess in original_word:
                
                letter_indices = occurance(original_word, modified_word, guess)
                if len(letter_indices) == 0:
                    print("Wrong Guess!!")
                    hang_visual_tracker += 1
                    print(v[hang_visual_tracker])                    
                    print("".join(modified_word))
                    continue

                print("Right Guess!!")
                if hang_visual_tracker > 1:
                    hang_visual_tracker -= 1
                    print(v[hang_visual_tracker])
                # print("indices: ", letter_indices)
                for index in letter_indices:
                    modified_word[index] = guess
            else:
                print("Wrong Guess!!")  
                print(v[hang_visual_tracker]) 
                hang_visual_tracker += 1             

            print("".join(modified_word))
            
            # After each loop, checking for won/not             
            if(original_word == modified_word):
                is_won = True 
                break    
        
        if is_won:
            print("HURRAY, You have won the game!!!")
        else:
            print("OH GOD, You have been hanged!!!")

        if input("Do you want to start new game??(y/n): ")   == "y":
            continue            

        break

    print("Thanks for playing!!")
    return 1


if __name__ == "__main__":
    play()
