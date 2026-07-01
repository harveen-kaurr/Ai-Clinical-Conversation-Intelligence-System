import streamlit as st

def create_kpi_card(
    title,
    value,
    color="#0d9488"
):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:18px;
            border-radius:12px;
            border-left:5px solid {color};
            box-shadow:0 2px 8px rgba(0,0,0,0.08);
            margin-bottom:10px;
        ">
            <h5 style="margin:0;color:#64748b;">
                {title}
            </h5>

            <h2 style="margin-top:10px;color:#1e293b;">
                {value}
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
def show_dashboard_page():
    st.title("AI Clinic Dashboard")

    st.markdown(
        "Welcome to the AI Clinical Conversation Intelligence Dashboard."
    )

    st.divider()

    st.subheader("Key Performance Indicators")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        create_kpi_card(
            "Patients",
            "--"
        )

    with kpi2:
        create_kpi_card(
            "Assessments",
            "--"
        )

    with kpi3:
        create_kpi_card(
            "Consultations",
            "--"
        )

    with kpi4:
        create_kpi_card(
            "Treatments",
            "--"
        )

    st.divider()

    left_column, right_column = st.columns([2, 1])

    with left_column:
        st.subheader("Patient Summary")
        st.info(
            "Patient summary will appear here after Supabase integration."
        )

    with right_column:
        st.subheader("Recent Activity")
        st.info("Recent activities will appear here.")

    st.divider()

    st.subheader("Analytics")
    st.info(
        "Charts and visualizations will be available in upcoming phases."
    )
    st.divider()

    st.subheader("Upcoming Features")

    st.write("- Patient Search")
    st.write("- Conversation History")
    st.write("- AI Analysis")
    st.write("- Progress Charts")
    st.write("- Reports")
