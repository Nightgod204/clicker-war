import streamlit as st
import time

st.set_page_config(page_title="Clicker War", page_icon="🖱️")
st.title("🖱️ Clicker War: 10-Second Blitz!")

# Initialize the game variables
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.start_time = None
    st.session_state.game_over = False

def handle_click():
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()
    if not st.session_state.game_over:
        st.session_state.count += 1

# Game logic: Check if time is up
if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    if elapsed >= 10:
        st.session_state.game_over = True

# Displaying the Game
if st.session_state.game_over:
    st.balloons()
    st.error(f"⏱️ TIME'S UP! Final Score: {st.session_state.count} clicks!")
    if st.button("Play Again"):
        st.session_state.count = 0
        st.session_state.start_time = None
        st.session_state.game_over = False
        st.rerun()
else:
    st.button("CLICK ME AS FAST AS YOU CAN!", on_click=handle_click, use_container_width=True)
    st.header(f"Score: {st.session_state.count}")
    
    if st.session_state.start_time:
        timer = max(0, 10 - elapsed)
        st.write(f"⏳ Time remaining: {round(timer, 1)} seconds")
    else:
        st.info("The timer starts as soon as you click!")
