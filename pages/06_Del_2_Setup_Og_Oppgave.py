import streamlit as st

from backend.domain.services.create_countries_df import prepare_country_data
from backend.infrastructure.rest_countries import fetch_countries_data
from frontend_widgets.bar_chart_widgets import (
    visualize_area_widget,
    visualize_population_widget,
)

st.title(":earth_africa: Global Countries Data Visualization")


st.header(":dart: Mål")
st.write(
    """
Målet for denne øvelsen er å teste hvordan det er å bygge en applikasjon ved bruk av streamlit. 
Bruk Streamlits mange "widgets" for å skape et brukervennlig grensesnitt som gjør datautforsking både informativt og visuelt.
"""
)


st.header(":writing_hand: Oppgave")
st.markdown(
    """
Din oppgave er å muliggjøre for sluttbruker å visuelt sammenligne to land. 
Lag interaktive visualiseringer som lar sluttbruker velge land, deretter vis en sammenlignende 
analyse som fremhever likheter, forskjeller og unike innsikter om de valgte landene."""
)


st.divider()
with st.spinner("Loading data"):
    countries_data = fetch_countries_data()
    df = prepare_country_data(countries_data)

st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

st.header("Population Visualization")
visualize_population_widget(df)

st.divider()

st.header("Area Visualization")
visualize_area_widget(df)
