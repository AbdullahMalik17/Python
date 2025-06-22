import streamlit as st
from words import words
import random 
import string

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice([w.upper() for w in words if '_' not in w and ' ' not in w])
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 6
    st.session_state.game_over = False

def reset_game():
    st.session_state.word = random.choice([w.upper() for w in words if '_' not in w and ' ' not in w])
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 6
    st.session_state.game_over = False

def main():
    st.title("🎮 Hangman Game")
    st.write("### Welcome! Try to guess the word one letter at a time.")
    
    # Display game state
    word_display = ' '.join(
        letter if letter in st.session_state.used_letters else '_' 
        for letter in st.session_state.word
    )
    
    # Create columns for game display
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### Word: {word_display}")
        st.write(f"Lives: {'❤️' * st.session_state.lives}")
    with col2:
        st.write("Used letters:")
        st.write(' '.join(sorted(st.session_state.used_letters)))
    
    # Handle user input if game is not over
    if not st.session_state.game_over:
        user_input = st.text_input(
            "Enter a letter:",
            key=f"guess_{len(st.session_state.used_letters)}",
            max_chars=1
        ).upper()
        
        if user_input:
            if user_input in string.ascii_uppercase:
                if user_input not in st.session_state.used_letters:
                    st.session_state.used_letters.add(user_input)
                    
                    if user_input in st.session_state.word_letters:
                        st.session_state.word_letters.remove(user_input)
                        st.success("Correct guess! 🎉")
                    else:
                        st.session_state.lives -= 1
                        st.warning("Wrong guess! 😢")
                else:
                    st.warning("You already guessed that letter!🔄 ")
            else:
                st.error("Please enter a valid letter! 🚫")
    
    # Check game end conditions
    if st.session_state.lives == 0:
        st.session_state.game_over = True
        st.error(f"Game Over! 💀 The word was: {st.session_state.word}")
    elif len(st.session_state.word_letters) == 0:
        st.session_state.game_over = True
        st.success(f"Congratulations! 🎉 You won with {st.session_state.lives} lives left!")
    
    # Play again button
    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game()
            st.experimental_rerun()

if __name__ == "__main__":
    main() 