import streamlit as st
from words import words
import random 
import string

if 'user_letter' not in st.session_state:
    st.session_state.user_letter = ''
if 'game_state' not in st.session_state:
    st.session_state.game_state = {}

st.title("Hangman Game")
st.write("Welcome to Hangman Game! Let's play!")
def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '_' in word or ' ' in word:
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
        word_list = [letter if letter in used_letters else '-' for letter in word]        
        st.write(list(map(lambda x: x if x in used_letters else '-', word)))
        st.write('Current word: ', ' '.join(word_list))
        st.write('Used letters: ', ' '.join(used_letters))
        st.write('Lives left: ', lives)
        st.write("_"*50)
    # get user input for letter
        user_letter = st.text_input('Guess a letter:', key='user_input').upper()
        if user_letter:  # Only process if user entered something
            st.session_state.user_letter = user_letter
        if user_letter in alphabets - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letter:
              word_letter.remove(user_letter)
           else:
              lives = lives - 1
              st.warning('Letter is not in the word.')   
        elif user_letter in used_letters:
           st.warning('You have already used that character. Please try again.')
        else:
           st.warning('Invalid character. Please try again.')
        # Replace the final if-else block with this enhanced version
    st.write("\n" + "="*50)
    if len(word_letter) == 0:
        st.write(f"""
🎉 Congratulations! 🎉
You've successfully guessed the word: {word}
Lives remaining: {lives}
        """)
    else:
        st.write(f"""
💀 Game Over! 💀
The word was: {word}
Better luck next time!
        """)
    print("="*50)
    
    play_again = st.text_input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        hangman()
    else:
        st.write("Thanks for playing! Goodbye!")         

hangman()