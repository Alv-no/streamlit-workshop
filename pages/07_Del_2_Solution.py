import streamlit as st

from backend.domain.services.create_countries_df import prepare_country_data
from backend.infrastructure.rest_countries import fetch_countries_data
from frontend_logic.session_state_logic import get_name_state
from frontend_widgets.no_name_widget import no_name_widget

no_name_widget()
st.title(f":blue[{get_name_state()}'s] Personal Solutions to the Task")
with st.spinner("Loading data"):
    countries_data = fetch_countries_data()
    df = prepare_country_data(countries_data)
