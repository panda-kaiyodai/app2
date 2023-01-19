import pandas as pd
import numpy as np
from scipy import optimize
import streamlit as st
import random

st.title("トランプゲーム")

# define a list of cards
cards = [i for i in range(2,11)] + ["J","Q","K","A"]*4

# shuffle the cards
random.shuffle(cards)

# Initialize the player's and the computer's hand
player_hand = []
computer_hand = []

# Deal the cards
for i in range(2):
    player_hand.append(cards.pop())
    computer_hand.append(cards.pop())

# Create a function to play the game
def play_game():
    # Show the player's and the computer's hand
    st.write("Your hand:", player_hand)
    st.write("Computer's hand:", computer_hand)

    # Get the user's choice
    choice = st.selectbox("Choose a card to throw away:", player_hand)

    # Discard the card
    player_hand.remove(choice)

    # Draw a new card
    player_hand.append(cards.pop())

    # Check for a win
    if player_hand == []:
        st.write("You win!")
    else:
        st.write("Your hand:", player_hand)

# Create a start button
if st.button("Start"):
    play_game()
