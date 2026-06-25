import streamlit as st
import pandas as pd
from services.treatment_crud import get_all_treatments

def show_view_treatment_page():
    st.markdown('<h2 class="gradient-header">View Treatment History</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">List of all logged patient treatment sessions, including physical manipulation records and Ayurvedic therapies.</p>', unsafe_allow_html=True)

    with st.spinner("Loading treatment logs..."):
        treatments = get_all_treatments()

    if not treatments:
        st.info("No treatment logs found in the database.")
        return

    df = pd.DataFrame(treatments)

    total_sessions = len(df)
    unique_consultations = df['consultation_id'].nunique() if 'consultation_id' in df.columns else 0
    improved_count = len(df[df['treatment_status'].astype(str).str.lower() == 'improved']) if 'treatment_status' in df.columns else 0

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Treatment Sessions", f"{total_sessions}")
    with m2:
        st.metric("Patients Under Care", f"{unique_consultations}")
    with m3:
        st.metric("Improvement Rate", f"{round((improved_count / total_sessions) * 100, 1) if total_sessions > 0 else 0}%")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">📋 Treatment Log Master list</h4>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
