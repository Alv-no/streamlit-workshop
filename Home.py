import streamlit as st
from frontend_logic.session_state_logic import (
    get_name_state,
    init_name_state,
    set_name_state,
)

from frontend_widgets.pause_widget import short_break_widget

# Page Configuration
st.set_page_config(page_title="Workshop #4", layout="wide")

# Front Page Title
st.title("🎓 Workshop #4, Streamlit med Øyvind og Fridtjof 🚀")

st.header("📅 Agenda - Oversikt")
st.markdown(
    """
- 🌟 Del 1: Intro
- 🛠️ Del 2: Setup og oppgave
- 🖥️ Del 3: Prøve å implementere selv
- ✨ Del 4: Vi implementerer løsningen
- 💬 Del 5: Diskusjon for potensielle caser
- 🚀 Del 6: Bygge noe eget eller bygge videre
"""
)

init_name_state()
name = st.text_input("Your name:")
if not get_name_state() and name:
    set_name_state(name)
    st.balloons()

# Detailed Agenda
with st.expander("📅 Agenda - Detaljert"):
    st.markdown(
        """
### 🌟 Del 1: Intro - 20 min
- **Streamlit**: Introduksjon
- **Komponenter**: Fra grunnleggende til avanserte
- **Konsepter**: State management og caching
- **Visualisering**: Hvordan elementer vises på siden
"""
    )

    short_break_widget()
    # Del 2: Setup og oppgave
    st.markdown(
        """
### 🛠️ Del 2: Setup og oppgave - 20 min
- **Case-presentasjon**: Utvikle en enkel applikasjon
- **Verktøy og oppsett**: Virtual environment og pip-tools
- **Oppgave**: Global Countries Data Visualization
"""
    )

    short_break_widget()

    # Del 3: Implementasjon
    st.markdown(
        """
### 🖥️ Del 3: Prøve å implementere selv - 60 min
Her vil dere får en liten case oppgave hvor dere skal bruke streamlit for å løse den.
"""
    )

    short_break_widget()

    # Del 4: Løsning
    st.markdown(
        """
### ✨ Del 4: Vi implementerer løsningen - 15 min
Gjennomgang av en løsning fra vår side, og potensiel presentasjon av deres funn og løsninger.
    """
    )

    short_break_widget()

    # Del 5: Diskusjon
    st.markdown(
        """
### 💬 Del 5: Diskusjon for potensielle caser - 15 min
Diskusjon rundt bruk og potensielle applikasjoner
    """
    )

    # Del 6: Egen utvikling
    st.markdown(
        """
### 🚀 Del 6: Bygge noe eget eller bygge videre - resten
Fritid for videre utforskning
    """
    )

    # Footer
    st.divider()
    st.write("👋 Lykke til med workshoppen!")
