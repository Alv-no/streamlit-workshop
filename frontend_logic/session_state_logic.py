import streamlit as st

from frontend_logic import State


def init_image_number_state() -> None:
    if State.IMAGE_NUMBER not in st.session_state:
        st.session_state[State.IMAGE_NUMBER] = 0


def get_image_number_state() -> int:
    return st.session_state[State.IMAGE_NUMBER]


def set_image_number_state(image_number: int) -> None:
    st.session_state[State.IMAGE_NUMBER] = image_number
