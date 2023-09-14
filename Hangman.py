import random
import string
from list_of_words import words
from life_dictionary  import life_dictionary_visual 


def  get_valid_word(words):
 
 word = random.choice(words)

 while "-" in word or " " in word:
    word = random.choice(words)

 return word.upper()    

def hangman():

    print("¡Welcome to Hangman!")

    word = get_valid_word(words)

    guess_letter = set(word)
    guessed_letter = set()
    alphabet = set(string.ascii_uppercase)

    life = 7

    while len(guess_letter) > 0 and life > 0:
       print(f"it left {life} and you used these letters: {' '.join(guessed_letter)}")

       wordlist = [letter if letter in guessed_letter else '-' for letter in word]
       print(life_dictionary_visual[life])
       print(f"word:{' '.join(wordlist)}")

       user_letter = input("Choose a letter: ").upper()

       if user_letter in alphabet - guessed_letter:
          guessed_letter.add(user_letter)
          if user_letter in guessed_letter:
             guess_letter.remove(user_letter)
             print(' ')
          else:
             life = life - 1 
             print(f"\nThis letter {user_letter} is not in the word")   
       elif user_letter in guessed_letter:
          print(f"\nYou already choose that letter. Choose a new one")

       else:
          print("\nThis letter is not valid")

    if life == 0:
       print(life_dictionary_visual[life])  
       print(f"¡You have been Hang. You lose")
       print(f"The word is: {word}")    
    else:
       print("¡You Won!") 

hangman()
                




