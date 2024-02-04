import streamlit as st

from frontend_logic import State


def init_image_number_state() -> None:
    """Initialize the image number state in Streamlit session state.

    This function checks if the image number state exists in Streamlit session state.
    If it doesn't exist, it initializes it to zero.

    Returns:
        None
    """
    if State.IMAGE_NUMBER not in st.session_state:
        st.session_state[State.IMAGE_NUMBER] = 0


def get_image_number_state() -> int:
    """Get the current image number state from Streamlit session state.

    Returns:
        int: The current image number state.
    """
    return st.session_state[State.IMAGE_NUMBER]


def set_image_number_state(image_number: int) -> None:
    """Set the image number state in Streamlit session state.

    Args:
        image_number (int): The new image number state to be set.

    Returns:
        None
    """
    st.session_state[State.IMAGE_NUMBER] = image_number


def set_name_state(name: str) -> None:
    """Set the user name state in Streamlit session state.

    Args:
        name (str): The user's name to be set as the state.

    Returns:
        None
    """
    st.session_state[State.NAME] = name


def get_name_state() -> str:
    """Get the current user name state from Streamlit session state.

    Returns:
        str: The current user's name.
    """
    return st.session_state.get(State.NAME, "")


def init_name_state() -> None:
    """Initialize the user name state in Streamlit session state.

    This function checks if the user name state exists in Streamlit session state.
    If it doesn't exist, it initializes it to an empty string.

    Returns:
        None
    """
    if State.NAME not in st.session_state:
        st.session_state[State.NAME] = ""
