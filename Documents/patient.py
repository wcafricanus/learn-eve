from mongoengine import Document, StringField, DateTimeField, IntField, FloatField

HANDEDNESS = ('left', 'right', 'both')


class Patient(Document):
    patient_id = StringField(required=True, primary_key=True)
    patient_name = StringField(required=True)
    dominant_hand = StringField(choices=HANDEDNESS)
    date_of_birth = DateTimeField(required=True)
    assessment_date = DateTimeField(required=True)
    stroke_severity_scale = IntField()
    disability_score_mRS = IntField()
    years_of_education = IntField()
    ethnicity = StringField()
    gender = StringField()
    onset_of_stroke = DateTimeField()
    setting_of_assessment = StringField()