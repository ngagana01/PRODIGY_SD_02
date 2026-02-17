import streamlit as st
import random

st.set_page_config(page_title="Guessing Game", page_icon="🎯", layout="centered")

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("Guess a number between **1 and 100**")

# Input field
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
