import streamlit as st
import random

st.set_page_config(page_title="Rock-Scissors-Paper", layout="centered")
st.title("🎮 Rock-Scissors-Paper Game")

choices = ["rock", "scissors", "paper"]

# Initialize session state
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0

st.sidebar.header("📊 Statistics")
st.sidebar.metric("Games Played", st.session_state.games_played)
st.sidebar.metric("Wins", st.session_state.wins)
st.sidebar.metric("Losses", st.session_state.losses)
st.sidebar.metric("Draws", st.session_state.draws)

# Game logic
st.subheader("Make Your Choice")
player_choice = st.selectbox("Select your choice:", choices)

if st.button("Play", use_container_width=True):
        computer_choice = random.choice(choices)
        
        # Determine winner
        if player_choice == computer_choice:
            result = "Draw 🤝"
            st.session_state.draws += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            result = "You Win! 🎉"
            st.session_state.wins += 1
        else:
            result = "You Lose! 😢"
            st.session_state.losses += 1
        
        st.session_state.games_played += 1
        
        # Display result
        st.success(f"**Your choice:** {player_choice.capitalize()}")
        st.info(f"**Computer choice:** {computer_choice.capitalize()}")
        st.warning(f"**Result:** {result}")

st.markdown("---")
if st.button("🔄 Reset Statistics", use_container_width=True):
    st.session_state.games_played = 0
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.rerun()
