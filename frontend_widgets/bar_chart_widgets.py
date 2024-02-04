import pandas as pd
import streamlit as st


def visualize_population_widget(df: pd.DataFrame):
    """Visualizes countries by population using a bar chart.

    Args:
        df (pd.DataFrame): A DataFrame containing country data with a 'Name' and 'Population' column.

    Example:
        visualize_population(df)

    This function creates a bar chart to visualize the top 10 countries with the highest population.
    """
    top_countries = df.nlargest(10, "Population")
    st.bar_chart(top_countries.set_index("Name")["Population"])


def visualize_area_widget(df: pd.DataFrame):
    """Visualizes countries by area using a bar chart.

    Args:
        df (pd.DataFrame): A DataFrame containing country data with a 'Name' and 'Area' column.

    Example:
        visualize_area(df)

    This function creates a bar chart to visualize the top 10 countries with the largest land area.
    """
    largest_countries = df.nlargest(10, "Area")
    st.bar_chart(largest_countries.set_index("Name")["Area"])
