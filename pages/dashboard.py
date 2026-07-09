import streamlit as st
import streamlit.components.v1 as components

from services.dashboard_service import (
    DashboardService
)


def create_kpi_card(
    title,
    value,
    color="#0d9488"
):

    st.markdown(
        f'<div style="background:white;padding:18px;border-radius:12px;border-left:5px solid {color};box-shadow:0 2px 8px rgba(0,0,0,0.08);margin-bottom:10px;">'
        f'<p style="margin:0;color:#64748b;font-size:14px;font-weight:600;">{title}</p>'
        f'<p style="margin-top:8px;color:#1e293b;font-size:28px;font-weight:700;line-height:1;">{value}</p>'
        f'</div>',
        unsafe_allow_html=True
    )


def show_dashboard_page():

    dashboard = (
        DashboardService
        .get_dashboard_statistics()
    )

    st.title(
        "AI Clinic Dashboard"
    )

    st.markdown(
        "Welcome to the AI Clinical Conversation Intelligence Dashboard."
    )

    st.divider()

    st.subheader(
        "Key Performance Indicators"
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        create_kpi_card(
            "Patients",
            dashboard["patients"]
        )

    with kpi2:

        create_kpi_card(
            "Assessments",
            dashboard["assessments"]
        )

    with kpi3:

        create_kpi_card(
            "Consultations",
            dashboard["consultations"]
        )

    with kpi4:

        create_kpi_card(
            "Treatments",
            dashboard["treatments"]
        )

    st.divider()

    kpi5, kpi6, kpi7 = st.columns(3)

    with kpi5:

        create_kpi_card(
            "Progress Records",
            dashboard["progress"],
            "#3b82f6"
        )

    with kpi6:

        create_kpi_card(
            "Conversations",
            dashboard["conversations"],
            "#8b5cf6"
        )

    with kpi7:

        create_kpi_card(
            "AI Analysis",
            dashboard["ai_analysis"],
            "#f59e0b"
        )

    st.divider()

    left_column, right_column = st.columns(
        [2, 1]
    )

    with left_column:

        st.subheader(
            "Recent Patients"
        )

        if dashboard["recent_patients"]:

            for patient in dashboard[
                "recent_patients"
            ]:

                st.write(
                    f"• {patient['patient_name']}"
                )

        else:

            st.info(
                "No patient records available."
            )

    with right_column:

        st.subheader(
            "Recent Consultations"
        )

        if dashboard[
            "recent_consultations"
        ]:

            for consultation in dashboard[
                "recent_consultations"
            ]:

                st.write(
                    f"• {consultation['doctor_name']}"
                )

        else:

            st.info(
                "No consultation records available."
            )

    st.divider()

    st.subheader(
        "Recent Treatments"
    )

    if dashboard[
        "recent_treatments"
    ]:

        for treatment in dashboard[
            "recent_treatments"
        ]:

            st.write(
                f"• {treatment['treatment_type']}"
            )

    else:

        st.info(
            "No treatment records available."
        )

    st.divider()

    st.markdown("""
### 📊 Power BI Clinical Analytics Dashboard

<a href="https://app.powerbi.com/groups/me/reports/09ad6c79-6bd4-4f3c-838a-8038f68bb966/90b40ac04f4ca46c3e10?experience=power-bi"
target="_blank">
<button style="
padding:12px 30px;
background:#2563eb;
color:white;
border:none;
border-radius:8px;
font-size:16px;
cursor:pointer;">
Open Dashboard
</button>
</a>
""", unsafe_allow_html=True)
    if "error" in dashboard:

        st.error(
            dashboard["error"]
        )