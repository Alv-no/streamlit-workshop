import streamlit as st

from frontend_widgets.display_image_widget import display_images_widget


# Page Configuration
st.set_page_config(page_title="Workshop #4", layout="wide")
FILE_PATHS: list[str] = ["data/fullstack_app.png", "data/streamlit.png"]
# Front Page Title
st.title("🌟 Del 1: Intro")
st.divider()

st.write("### Hva er egentlig Streamlit?")
display_images_widget(FILE_PATHS)
