import streamlit as st
import numpy as np

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# Initialize game state
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "winner" not in st.session_state:
    st.session_state.winner = None

# -----------------------------
# Game Logic functions
# -----------------------------
def check_winner(b):
    row_sum = np.sum(b, axis=1)
    col_sum = np.sum(b, axis=0)

    if 3 in row_sum or 3 in col_sum:
        return "X"
    if -3 in row_sum or -3 in col_sum:
        return "O"

    if np.trace(b) == 3:
        return "X"
    if np.trace(b) == -3:
        return "O"

    if np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(np.fliplr(b)) == -3:
        return "O"

    if not np.any(b == 0):
        return "DRAW"

    return None

def make_move(row, col):
    if st.session_state.game_over:
        return
    if st.session_state.board[row, col] != 0:
        return

    st.session_state.board[row, col] = st.session_state.current
    result = check_winner(st.session_state.board)

    if result is not None:
        st.session_state.winner = result
        st.session_state.game_over = True
    else:
        st.session_state.current *= -1

def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.winner = None

# -----------------------------
# UI Header & Status
# -----------------------------
st.title("🎮 Tic Tac Toe")
st.write("Built with Python, NumPy & Streamlit")
st.divider()

if not st.session_state.game_over:
    player = "X" if st.session_state.current == 1 else "O"
    st.subheader(f"Current Player: {player}")
else:
    if st.session_state.winner == "DRAW":
        st.subheader("🤝 It's a Draw!")
    else:
        st.subheader(f"🏆 Player {st.session_state.winner} Wins!")

st.write("")

# -----------------------------
# Game Board
# -----------------------------
symbols = {
    0: "",
    1: "❌",
    -1: "⭕"
}

for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        value = st.session_state.board[r, c]
        disabled = value != 0 or st.session_state.game_over

        if cols[c].button(
            symbols[value] if symbols[value] else "   ",
            key=f"cell_{r}_{c}",
            disabled=disabled,
            use_container_width=True
        ):
            make_move(r, c)
            st.rerun()

st.write("")

# -----------------------------
# Reset Button
# -----------------------------
if st.button("🔄 Restart Game", use_container_width=True):
    reset_game()
    st.rerun()