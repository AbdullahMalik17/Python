from words import words
import random 
import string
def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word = get_valid_word(words)    
    word_letter = set(word) #letters in the words
    alphabets = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 5

   # Giving letter from the user
    while len(word_letter) > 0 and lives > 0:
        word_list = list(map(lambda x: x if x in used_letters else '-', word))
        print('Current word: ', ' '.join(word_list))
        print('Used letters: ', ' '.join(used_letters))
        print('Lives left: ', lives)
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabets - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letter:
              word_letter.remove(user_letter)
           else:
              lives = lives - 1
              print('Letter is not in the word.')   
        elif user_letter in used_letters:
           print('You have already used that character. Please try again.')
        else:
           print('Invalid character. Please try again.')
    if word_letter == used_letters:
        print('Congratulations! You have guessed Corect word:',word)
    else:
            print('Sorry! You have lost the game. The word was:',word)          
    
hangman()        
    