import streamlit as st


WINNERS = [
    (0, 1, 2),( 3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "player" not in st.session_state:
    st.session_state.player = "X"

if "winner" not in st.session_state:
    st.session_state.winner = None

if "draw" not in st.session_state:
    st.session_state.draw = False


def check_winner():
    board = st.session_state.board
    for a, b, c in WINNERS:
        if (
            board[a] != ""
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            st.session_state.winner = board[a]
            return
    if "" not in board:
        st.session_state.draw = True


def make_move(index):
    if (
        st.session_state.board[index] == ""
        and st.session_state.winner is None
        and not st.session_state.draw
    ):
        st.session_state.board[index] =(
            st.session_state.player
        )

        check_winner()

        if (
            st.session_state.winner is None
            and not st.session_state.draw
        ):
            st.session_state.player = (
                "O"
                if st.session_state.player == "X"
                else "X"
            )


def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = None
    st.session_state.draw = False


st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮"
)

st.title("🎮 Tic Tac Toe")

if st.session_state.winner:
    st.success(
        f"Player {st.session_state.winner} Wins!"
    )
elif st.session_state.draw:

    st.warning("Draw!")
else:
    st.info(
        f"Player Turn: {st.session_state.player}"
    )


for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col
        symbol = (
            st.session_state.board[index]
            if st.session_state.board[index]
            else " "
        )

        with cols[col]:
            st.button(
                symbol,
                key=index,
                on_click=make_move,
                args=(index,),
                use_container_width=True
            )


st.write("---")

if st.button(
    "🔄 New Game",
    use_container_width=True
):
    reset_game()
    st.rerun()      

