import streamlit as st

from frontend_logic.session_state_logic import get_name_state


def no_name_widget() -> None:
    """
    Displays a warning message and a link to the homepage if the user's name has not been entered.

    This function checks if the user has provided their name via `get_name_state()`. If not, it displays a warning message
    with instructions to return to the homepage to input their name. A container with a link to the homepage is also created
    to facilitate easy navigation back.

    The function utilizes Streamlit's warning and container components to create a visually engaging alert that guides the user
    on the necessary action to take. The use of emojis and Markdown enhances the readability and user engagement with the
    warning message.

    Returns:
        None: This function returns nothing and is used solely for displaying a UI element in a Streamlit application.

    Note:
        - `get_name_state()` should be defined elsewhere in the codebase and is expected to return a boolean value indicating
          whether the user's name has been set.
        - `page_link()` is not a default Streamlit function and may represent a custom implementation for navigating to
          different pages within the app. Ensure this function or its equivalent is properly defined to avoid runtime errors.
    """
    if not get_name_state():
        c = st.container(border=True)
        st.warning(
            """
            ### :warning: Oops! It looks like you forgot to enter your name. 📝
            
            To proceed, please ensure you input your name. Click the button below to return to the homepage and complete the necessary steps. 🏠
            
            :point_down: **Go Back to Homepage** 
            """
        )
        c = st.container(border=True)
        c.page_link(
            "Home.py", label="Go to homepage", icon="🏠", use_container_width=True
        )
