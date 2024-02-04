import streamlit as st
import pandas as pd

from data.example_df import example_data_dict

# Display Data Components 📊
st.header("Display Data Components 📊")

st.divider()

# DataFrame
st.subheader("DataFrame:")
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
my_dataframe = pd.DataFrame(data)
st.dataframe(my_dataframe)
""",
    language="python",
)
st.write(":eyes: **Displays:**")

my_dataframe = pd.DataFrame(example_data_dict)
st.dataframe(my_dataframe, use_container_width=True)

st.divider()

# Table
st.subheader("Table:")
st.write(":snake: **Python Code:**")
st.code(
    """
# Assuming `data` is a pandas DataFrame as defined above
st.table(my_dataframe.iloc[0:10])
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.table(my_dataframe.iloc[0:10])

st.divider()

# JSON
st.subheader("JSON:")
st.write(":snake: **Python Code:**")
st.code(
    """
st.json({'foo':'bar', 'fu':'ba'})
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.json({"foo": "bar", "fu": "ba"})

st.divider()

# Metric
st.subheader("Metric:")
st.write(":snake: **Python Code:**")
st.code(
    """
st.metric(label="Temperature", value="273 K", delta="1.2 K")
""",
    language="python",
)
st.write(":eyes: **Displays:**")
st.metric(label="Temperature", value="273 K", delta="1.2 K")
