import streamlit as st
import time

# Dynamic Components 🔄
st.header("Dynamic Components 🔄")

st.divider()

# Spinner
st.subheader("Spinner:")
st.write(":snake: **Python Code:**")
st.code(
    """
with st.spinner(text='In progress'):
    time.sleep(3)
    st.success('Done')
""",
    language="python",
)
st.write(":eyes: **Displays:**")
if st.button("Start Spinner"):
    with st.spinner(text="In progress"):
        time.sleep(3)
        st.success("Done")

st.divider()

# Progress Bar
st.subheader("Progress Bar:")
st.write(":snake: **Python Code:**")
st.code(
    """
bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    bar.progress(percent_complete + 1)
""",
    language="python",
)
st.write(":eyes: **Displays:**")
if st.button("Show Progress Bar"):
    bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        bar.progress(percent_complete + 1)

st.divider()

# Balloons
st.subheader("Balloons:")
st.write(":snake: **Python Code:**")
st.code("st.balloons()", language="python")
st.write(":eyes: **Displays:**")
if st.button("Release Balloons"):
    st.balloons()

st.divider()

# Snow
st.subheader("Snow:")
st.write(":snake: **Python Code:**")
st.code("st.snow()", language="python")
st.write(":eyes: **Displays:**")
if st.button("Let it Snow"):
    st.snow()

st.divider()

# Toast
st.subheader("Toast Notification:")
st.write(":snake: **Python Code:**")
st.code('st.toast("Mr Stay-Puft")', language="python")
st.write(":eyes: **Displays:**")
if st.button("Show Toast"):
    st.toast("Mr Stay-Puft")

st.divider()

# Error Message
st.subheader("Error Message:")
st.write(":snake: **Python Code:**")
st.code('st.error("Error message")', language="python")
st.write(":eyes: **Displays:**")
st.error("Error message")

st.divider()

# Warning Message
st.subheader("Warning Message:")
st.write(":snake: **Python Code:**")
st.code('st.warning("Warning message")', language="python")
st.write(":eyes: **Displays:**")
st.warning("Warning message")

st.divider()

# Info Message
st.subheader("Info Message:")
st.write(":snake: **Python Code:**")
st.code('st.info("Info message")', language="python")
st.write(":eyes: **Displays:**")
st.info("Info message")

st.divider()

# Success Message
st.subheader("Success Message:")
st.write(":snake: **Python Code:**")
st.code('st.success("Success message")', language="python")
st.write(":eyes: **Displays:**")
st.success("Success message")
