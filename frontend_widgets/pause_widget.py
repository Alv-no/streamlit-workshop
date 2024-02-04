import streamlit as st


def short_break_widget() -> None:
    """
    Displays a short break message within a Streamlit application.

    This function creates a visual divider, displays a message indicating a short break
    (ranging from 5 to 15 minutes), and then adds another visual divider. It's designed
    to be used in a Streamlit application to denote breaks in the content or sections.

    Returns:
        None: This function does not return any value. It directly renders content in a Streamlit app.
    """
    st.divider()
    st.write("#### ⏰ Pause 5-15 min")
    st.divider()
