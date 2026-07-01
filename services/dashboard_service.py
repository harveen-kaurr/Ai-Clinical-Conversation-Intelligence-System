from services.patient_crud import (
    get_all_patients
)

from services.pain_assessment_crud import (
    get_all_assessments
)

from services.consultation_crud import (
    get_all_consultations
)

from services.treatment_crud import (
    get_all_treatments
)

from services.progress_crud import (
    get_all_progress
)

from services.conversation_crud import (
    get_all_conversations
)

from services.ai_crud import (
    get_all_analysis
)


class DashboardService:


    @staticmethod
    def get_dashboard_statistics():

        try:

            patients = get_all_patients()

            assessments = get_all_assessments()

            consultations = get_all_consultations()

            treatments = get_all_treatments()

            progress = get_all_progress()

            conversations = get_all_conversations()

            ai_analysis = get_all_analysis()

            return {

                "patients": len(
                    patients
                ) if patients else 0,

                "assessments": len(
                    assessments
                ) if assessments else 0,

                "consultations": len(
                    consultations
                ) if consultations else 0,

                "treatments": len(
                    treatments
                ) if treatments else 0,

                "progress": len(
                    progress
                ) if progress else 0,

                "conversations": len(
                    conversations
                ) if conversations else 0,

                "ai_analysis": len(
                    ai_analysis
                ) if ai_analysis else 0,

                "recent_patients": (
                    patients[-5:]
                    if patients
                    else []
                ),

                "recent_consultations": (
                    consultations[-5:]
                    if consultations
                    else []
                ),

                "recent_treatments": (
                    treatments[-5:]
                    if treatments
                    else []
                )

            }

        except Exception as error:

            return {

                "patients": 0,

                "assessments": 0,

                "consultations": 0,

                "treatments": 0,

                "progress": 0,

                "conversations": 0,

                "ai_analysis": 0,

                "recent_patients": [],

                "recent_consultations": [],

                "recent_treatments": [],

                "error": str(
                    error
                )

            }