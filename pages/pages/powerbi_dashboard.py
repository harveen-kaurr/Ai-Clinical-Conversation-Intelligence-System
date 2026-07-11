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

POWERBI_URL = "https://app.powerbi.com/groups/me/reports/d772f056-8e72-44f2-9e5a-858f13b2751f/7f7e694044448ee16bd4?experience=power-bi"

components.iframe(
    POWERBI_URL,
    height=900,
    scrolling=True
)
