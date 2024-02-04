import json

import numpy as np
import pandas as pd
import streamlit as st

from data.example_df import example_data_dict

# Interactive Components 🛠️
st.header("Interactive Components 🛠️")

st.divider()

# Button
st.subheader("Button:")
st.write(":snake: **Python Code:**")
st.code('st.button("Hit me")', language="python")
st.write(":eyes: **Displays:**")
st.button("Hit me")

st.divider()

st.subheader("Data Editor:")
st.write(":snake: **Python Code:**")
st.code(
    """
import pandas as pd
data = {
    'Name': ['Anna', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London'],
    'Occupation': ['Engineer', 'Doctor', 'Artist'],
    'Hobbies': ['Reading', 'Traveling', 'Painting']
}
st.data_editor('Edit data', pd.DataFrame(data), use_container_width=True)
""",
    language="python",
)
st.write(":eyes: **Displays:**")
# Data Preparation
my_dataframe = pd.DataFrame(example_data_dict)
st.data_editor(my_dataframe, use_container_width=True)

st.divider()

# Checkbox
st.subheader("Checkbox:")
st.write(":snake: **Python Code:**")
st.code('st.checkbox("Check me out")', language="python")
st.write(":eyes: **Displays:**")
st.checkbox("Check me out")

st.divider()

# Radio
st.subheader("Radio Buttons:")
st.write(":snake: **Python Code:**")
st.code('st.radio("Pick one:", ["nose", "ear"])', language="python")
st.write(":eyes: **Displays:**")
st.radio("Pick one:", ["nose", "ear"])

st.divider()

# Selectbox
st.subheader("Selectbox:")
st.write(":snake: **Python Code:**")
st.code('st.selectbox("Select", [1, 2, 3])', language="python")
st.write(":eyes: **Displays:**")
st.selectbox("Select", [1, 2, 3])

st.divider()

# Multiselect
st.subheader("Multiselect:")
st.write(":snake: **Python Code:**")
st.code('st.multiselect("Multiselect", [1, 2, 3])', language="python")
st.write(":eyes: **Displays:**")
st.multiselect("Multiselect", [1, 2, 3])

st.divider()

# Slider
st.subheader("Slider:")
st.write(":snake: **Python Code:**")
st.code('st.slider("Slide me", min_value=0, max_value=10)', language="python")
st.write(":eyes: **Displays:**")
st.slider("Slide me", min_value=0, max_value=10)

st.divider()

# Select Slider
st.subheader("Select Slider:")
st.write(":snake: **Python Code:**")
st.code('st.select_slider("Slide to select", options=[1, "2"])', language="python")
st.write(":eyes: **Displays:**")
st.select_slider("Slide to select", options=[1, "2"])

st.divider()

# Text Input
st.subheader("Text Input:")
st.write(":snake: **Python Code:**")
st.code('st.text_input("Enter some text")', language="python")
st.write(":eyes: **Displays:**")
st.text_input("Enter some text")

st.divider()

# Number Input
st.subheader("Number Input:")
st.write(":snake: **Python Code:**")
st.code('st.number_input("Enter a number")', language="python")
st.write(":eyes: **Displays:**")
st.number_input("Enter a number")

st.divider()

# Text Area
st.subheader("Text Area:")
st.write(":snake: **Python Code:**")
st.code('st.text_area("Area for textual entry")', language="python")
st.write(":eyes: **Displays:**")
st.text_area("Area for textual entry")

st.divider()

# Date Input
st.subheader("Date Input:")
st.write(":snake: **Python Code:**")
st.code('st.date_input("Date input")', language="python")
st.write(":eyes: **Displays:**")
st.date_input("Date input")

st.divider()

# Time Input
st.subheader("Time Input:")
st.write(":snake: **Python Code:**")
st.code('st.time_input("Time entry")', language="python")
st.write(":eyes: **Displays:**")
st.time_input("Time entry")

st.divider()

# File Uploader
st.subheader("File Uploader:")
st.write(":snake: **Python Code:**")
st.code('st.file_uploader("File uploader")', language="python")
st.write(":eyes: **Displays:**")
st.file_uploader("File uploader")

st.divider()

# Download Button
st.subheader("Download Button:")
st.write(":snake: **Python Code:**")
st.code(
    """
import json
data = {
    'Name': ['Anna', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London'],
    'Occupation': ['Engineer', 'Doctor', 'Artist'],
    'Hobbies': ['Reading', 'Traveling', 'Painting']
}
st.download_button("Download Data", json.dumps(data))
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.download_button("Download Data", json.dumps(example_data_dict))
st.divider()

# Camera Input
st.subheader("Camera Input:")
st.write(":snake: **Python Code:**")
st.code('st.camera_input("Camera input")', language="python")
st.write(":eyes: **Displays:**")
st.camera_input("Camera input")

st.divider()

# Color Picker
st.subheader("Color Picker:")
st.write(":snake: **Python Code:**")
st.code('st.color_picker("Pick a color")', language="python")
st.write(":eyes: **Displays:**")
st.color_picker("Pick a color")

st.divider()

# Subheader for the map
st.subheader("Map:")

# Displaying the Python code for a color picker as an example
st.write(":snake: **Python Code:**")
st.code(
    """
import numpy as np

np.random.seed(42)  # For reproducible results
n = 10  # Number of points
latitudes = np.random.uniform(low=57.9, high=71.2, size=n)
longitudes = np.random.uniform(low=4.8, high=31.2, size=n)

# Creating a DataFrame with these points
data = pd.DataFrame({"lat": latitudes, "lon": longitudes})


st.map(data)
    """,
    language="python",
)

np.random.seed(42)  # For reproducible results
n = 10  # Number of points
latitudes = np.random.uniform(low=57.9, high=71.2, size=n)
longitudes = np.random.uniform(low=4.8, high=31.2, size=n)

# Creating a DataFrame with these points
data = pd.DataFrame({"lat": latitudes, "lon": longitudes})

# Display the map with random points in Norway
st.write(":eyes: **Displays:**")
st.map(data)
