import streamlit as st
from pages.ai_analysis_dashboard import (
    show_ai_analysis_dashboard
)
from pages.conversation_history_dashboard import (
    show_conversation_history_dashboard
)
from pages.dashboard import show_dashboard_page
from pages.add_patient import (
    show_add_patient_page
)

from pages.view_patients import (
    show_view_patients_page
)

from pages.search_patient import (
    show_search_patient_page
)

from pages.edit_patient import (
    show_edit_patient_page
)

from pages.delete_patient import (
    show_delete_patient_page
)

from pages.add_assessment import (
    show_add_assessment_page
)

from pages.view_assessment import (
    show_view_assessment_page
)

from pages.search_assessment import (
    show_search_assessment_page
)

from pages.edit_assessment import (
    show_edit_assessment_page
)

from pages.delete_assessment import (
    show_delete_assessment_page
)

from pages.add_consultation import (
    show_add_consultation_page
)

from pages.view_consultation import (
    show_view_consultation_page
)

from pages.search_consultation import (
    show_search_consultation_page
)

from pages.edit_consultation import (
    show_edit_consultation_page
)

from pages.delete_consultation import (
    show_delete_consultation_page
)

from pages.view_ai_analysis import (
    show_view_ai_analysis_page
)
from pages.generate_ai_analysis import (
    show_generate_ai_analysis_page
)
from pages.generate_ai_analysis import (
    show_generate_ai_analysis_page
)

from pages.search_ai_analysis import (
    show_search_ai_analysis_page
)

from pages.ai_dashboard import (
    show_ai_dashboard_page
)

from pages.add_treatment import show_add_treatment_page
from pages.view_treatment import show_view_treatment_page
from pages.search_treatment import show_search_treatment_page
from pages.edit_treatment import show_edit_treatment_page
from pages.delete_treatment import show_delete_treatment_page

from pages.add_conversation import show_add_conversation_page
from pages.view_conversation import show_view_conversation_page
from pages.search_conversation import show_search_conversation_page
from pages.edit_conversation import show_edit_conversation_page
from pages.delete_conversation import show_delete_conversation_page

from pages.add_progress import show_add_progress_page
from pages.view_progress import show_view_progress_page
from pages.search_progress import show_search_progress_page
from pages.edit_progress import show_edit_progress_page
from pages.delete_progress import show_delete_progress_page

def inject_custom_css():
    st.markdown("""
    <style>
    /* Hide Streamlit default sidebar page list */
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Global styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #f8fafc;
    }
    
    /* Premium card container styling */
    .custom-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    
    .gradient-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
        display: inline-block;
    }

    .sidebar-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 15px;
        border-radius: 8px;
        color: white;
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid #334155;
    }

    .metric-card {
        background: #ffffff;
        border-left: 5px solid #0d9488;
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
        margin-bottom: 12px;
    }
    
    /* Custom button styling */
    .stButton>button {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%) !important;
        color: white !important;
        border: none !important;
        padding: 8px 20px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px -1px rgba(59, 130, 246, 0.4) !important;
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%) !important;
    }

    /* Warning/Delete Button Custom Styling */
    div.stButton > button[data-baseweb="button"]:has(span:contains("Delete")), 
    div.stButton > button[data-baseweb="button"]:has(span:contains("Confirm Delete")) {
        background: linear-gradient(135deg, #dc2626 0%, #f87171 100%) !important;
        box-shadow: 0 4px 6px -1px rgba(220, 38, 38, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Clinical Intelligence System",
    layout="wide"
)

inject_custom_css()

# Sidebar branding header
st.sidebar.markdown(
    """
    <div class="sidebar-header">
        <h3 style="margin:0; font-weight:700;">🏥 AI Clinical</h3>
        <p style="margin:0; font-size:0.8rem; opacity:0.8;">Intelligence Platform</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%); padding: 25px; border-radius: 12px; color: white; margin-bottom: 25px;">
        <h1 style="margin:0; font-weight:800; font-size: 2.2rem;">🏥 AI Clinical Intelligence System</h1>
        <p style="margin: 5px 0 0 0; opacity:0.9; font-size:1.1rem;">Healthcare analytics and patient management platform with AI-driven intelligence</p>
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.title("Navigation")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Patient Management",
        "Pain Assessment",
        "Consultation Management",
        "Treatment Management",
        "Conversation Capture",
        "Progress Management",
        "AI Analysis"
    ]
)

if module == "Dashboard":
    dashboard_page = st.sidebar.radio(
        "Dashboard",
        [
            "Overview",
            "Conversation History",
            "AI Analysis Dashboard"
        ]
    )


elif module == "Patient Management":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Patient",
            "View Patients",
            "Search Patient",
            "Edit Patient",
            "Delete Patient"
        ]
    )

elif module == "Pain Assessment":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Assessment",
            "View Assessment",
            "Search Assessment",
            "Edit Assessment",
            "Delete Assessment"
        ]
    )

elif module == "Consultation Management":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Consultation",
            "View Consultation",
            "Search Consultation",
            "Edit Consultation",
            "Delete Consultation"
        ]
    )

elif module == "Treatment Management":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Treatment",
            "View Treatment",
            "Search Treatment",
            "Edit Treatment",
            "Delete Treatment"
        ]
    )
elif module == "Progress Management":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Progress",
            "View Progress",
            "Search Progress",
            "Edit Progress",
            "Delete Progress"
        ]
    )

elif module == "Conversation Capture":
    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Conversation",
            "View Conversation",
            "Search Conversation",
            "Edit Conversation",
            "Delete Conversation"
        ]
    )

elif module == "AI Analysis":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Generate AI Analysis",
            "View AI Analysis",
            "Search AI Analysis",
            "AI Dashboard"
        ]
    )    


# Render Sidebar Stats
from services.patient_crud import get_all_patients
try:
    patients_data = get_all_patients()
    total_pat = len(patients_data) if patients_data else 0
except Exception:
    total_pat = 0

st.sidebar.markdown(f"""
<div style="background: #1e293b; padding: 16px; border-radius: 8px; border: 1px solid #334155; margin-top: 30px; color: white;">
    <h4 style="margin: 0 0 10px 0; font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; font-weight:700; letter-spacing: 0.5px;">System Stats</h4>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span style="font-size: 0.9rem; color: #cbd5e1;">Total Patients:</span>
        <span style="font-weight: 700; color: #38bdf8; font-size: 1.1rem;">{total_pat}</span>
    </div>
    <div style="font-size: 0.75rem; color: #64748b; border-top: 1px solid #334155; padding-top: 8px; text-align: center;">
        Database Status: <span style="color: #4ade80; font-weight:600;">CONNECTED</span>
    </div>
</div>
""", unsafe_allow_html=True)

if module == "Dashboard":

    if dashboard_page == "Overview":

        show_dashboard_page()

    elif dashboard_page == "Conversation History":

        show_conversation_history_dashboard()

    elif dashboard_page == "AI Analysis Dashboard":

        show_ai_analysis_dashboard()
# Patient Pages

elif page == "Add Patient":

    show_add_patient_page()

elif page == "View Patients":

    show_view_patients_page()

elif page == "Search Patient":

    show_search_patient_page()

elif page == "Edit Patient":

    show_edit_patient_page()

elif page == "Delete Patient":

    show_delete_patient_page()

# Assessment Pages

elif page == "Add Assessment":

    show_add_assessment_page()

elif page == "View Assessment":

    show_view_assessment_page()

elif page == "Search Assessment":

    show_search_assessment_page()

elif page == "Edit Assessment":

    show_edit_assessment_page()

elif page == "Delete Assessment":

    show_delete_assessment_page()

#Consultation Page    

elif page == "Add Consultation":

    show_add_consultation_page() 

elif page == "View Consultation":

    show_view_consultation_page()  

elif page == "Search Consultation":

    show_search_consultation_page()         

elif page == "Edit Consultation":

    show_edit_consultation_page()

elif page == "Delete Consultation":

    show_delete_consultation_page()

# Treatment Pages
elif page == "Add Treatment":
    show_add_treatment_page()

elif page == "View Treatment":
    show_view_treatment_page()

elif page == "Search Treatment":
    show_search_treatment_page()

elif page == "Edit Treatment":
    show_edit_treatment_page()

elif page == "Delete Treatment":
    show_delete_treatment_page()

# Conversation Pages
elif page == "Add Conversation":
    show_add_conversation_page()

elif page == "View Conversation":
    show_view_conversation_page()

elif page == "Search Conversation":
    show_search_conversation_page()

elif page == "Edit Conversation":
    show_edit_conversation_page()

elif page == "Delete Conversation":
    show_delete_conversation_page()
# Progress Pages

elif page == "Add Progress":

    show_add_progress_page()

elif page == "View Progress":

    show_view_progress_page()

elif page == "Search Progress":

    show_search_progress_page()

elif page == "Edit Progress":

    show_edit_progress_page()

elif page == "Delete Progress":

    show_delete_progress_page()

#AI analysis page

# AI Analysis Pages

elif page == "Generate AI Analysis":

    show_generate_ai_analysis_page()

elif page == "View AI Analysis":

    show_view_ai_analysis_page()

elif page == "Search AI Analysis":

    show_search_ai_analysis_page()

elif page == "AI Dashboard":

    show_ai_dashboard_page()

