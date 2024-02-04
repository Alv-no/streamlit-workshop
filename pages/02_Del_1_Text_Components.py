import streamlit as st

# Basic Components
st.header("Text Components 🧩")

st.divider()

# Display text example
st.subheader("Display text:")
st.write(":snake: **Python Code:**")
st.code(
    """
st.text("Fixed width text")
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.text("Fixed width text")

st.divider()

# Markdown
st.subheader("Markdown:")
st.write(":snake: **Python Code:**")
st.code('st.markdown("_Markdown_")', language="python")
st.write(":eyes: **Displays:**")
st.markdown("_Markdown_")

st.divider()

# Caption
st.subheader("Caption:")
st.write(":snake: **Python Code:**")
st.code('st.caption("Balloons. Hundreds of them...")', language="python")
st.write(":eyes: **Displays:**")
st.caption("Balloons. Hundreds of them...")

st.divider()

# Latex
st.subheader("Latex:")
st.write(":snake: **Python Code:**")
st.code('st.latex(r" e^{i\\pi} + 1 = 0 ")', language="python")
st.write(":eyes: **Displays:**")
st.latex(r" e^{i\pi} + 1 = 0 ")

st.divider()

# Displaying various objects
st.subheader("Displaying various objects:")
st.write(":snake: **Python Code:**")
st.code(
    """
st.write("Most objects")  # df, err, func, keras!
st.write(["st", "is <", 3])
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.write("Most objects")  # Placeholder for actual objects
st.write(["st", "is <", 3])

st.divider()

# Titles and Headers
st.subheader("Titles and Headers:")
st.write(":snake: **Python Code:**")
st.code(
    """
st.title("My title")
st.header("My header")
st.subheader("My sub")
""",
    language="python",
)
st.divider()
st.write(":eyes: **Displays:**")
st.title("My title")
st.header("My header")
st.subheader("My sub")

# Code
st.subheader("Displaying code:")
st.write(":snake: **Python Code:**")
st.code('st.code("for i in range(8): foo()")', language="python")
st.write(":eyes: **Displays:**")
st.code("for i in range(8): foo()")
