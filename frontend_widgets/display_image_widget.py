import streamlit as st

from frontend_logic.session_state_logic import (
    get_image_number_state,
    init_image_number_state,
    set_image_number_state,
)


def display_images_widget(file_paths: list[str]) -> None:
    """
    Displays a series of images in a Streamlit app from the specified file paths.

    This function takes a list of file paths to images stored locally and displays them sequentially
    in a Streamlit app. It's designed to be used within a Streamlit page to showcase images, such as
    screenshots, diagrams, or photos relevant to the app's content.

    Args:
        image_paths (list[str]): A list of strings, where each string is a file path to an image.

    Returns:
        None. This function directly renders images to the Streamlit app interface.

    Example:
        To use this function in a Streamlit app, first import the function and then call it with a list of image file paths:

        ```python
        import streamlit as st
        from frontend_widgets.display_image_widget import display_images_widget

        # Page Configuration
        st.set_page_config(page_title="Workshop #4", layout="wide")

        # List of image file paths
        FILE_PATHS: list[str] = ["data/fullstack_app.png", "data/streamlit.png"]

        # Display the title and a divider
        st.title("🌟 Del 1: Intro")
        st.divider()

        # Introductory text
        st.write("### Hva er egentlig Streamlit?")

        # Display the images
        display_images_widget(FILE_PATHS)
        ```
    Note:

    """
    init_image_number_state()

    c = st.container(border=True, height=650)
    col1, col2, _ = st.columns([1, 1, 15])
    with col1:
        if st.button(
            "Back", key="back-image", help="This button takes you to the previous image"
        ):
            set_image_number_state(get_image_number_state() - 1)
    with col2:
        if st.button(
            "Next", key="next-image", help="This button takes you to the next image"
        ):
            set_image_number_state(get_image_number_state() + 1)

    c.image(file_paths[get_image_number_state() % len(file_paths)])
