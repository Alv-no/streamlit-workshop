import requests
import streamlit as st

from . import REST_COUNTRIES_ENDPOINT


@st.cache_data(ttl=60 * 60, show_spinner=False)
def fetch_countries_data() -> list[dict]:
    """Fetches data about countries from the REST Countries API.

    Returns:
        list[dict]: A list of dictionaries containing country data.
    """
    response = requests.get(REST_COUNTRIES_ENDPOINT)
    countries = response.json()
    return countries
