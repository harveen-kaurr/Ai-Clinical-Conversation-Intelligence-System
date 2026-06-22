class PainAssessment:

    def __init__(
        self,
        assessment_id,
        patient_id,
        pain_areas,
        pain_severity,
        posture,
        notes,
        created_at
    ):
        self.assessment_id = assessment_id
        self.patient_id = patient_id
        self.pain_areas = pain_areas
        self.pain_severity = pain_severity
        self.posture = posture
        self.notes = notes
        self.created_at = created_at