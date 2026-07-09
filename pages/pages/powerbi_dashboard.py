import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Power BI Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Clinical Analytics Dashboard")

st.markdown(
    "View the interactive Power BI analytics dashboard below."
)

POWERBI_URL = "https://app.powerbi.com/groups/me/reports/09ad6c79-6bd4-4f3c-838a-8038f68bb966/90b40ac04f4ca46c3e10?experience=power-bi"

components.iframe(
    POWERBI_URL,
    height=900,
    scrolling=True
)