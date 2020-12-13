from db import db

class SurveyLocationModel(db.Model):
    __tablename__ = 'survey_locations'

    id = db.Column(db.Integer,primary_key = True)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.survey_id'))
    location_id = db.Column(db.Integer,db.ForeignKey('locations.id'))
    # survey = db.relationship("SurveyModel")
    # location = db.relationship("LocationModel")

    # locations = db.relationship('SurveyModel', lazy= 'dynamic')

    def __init__(self,survey_id,location_id):
        self.survey_id = survey_id
        self.location_id = location_id

    def json(self):
        return {"survey_id":self.survey_id,"location_id":self.location_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_survey_id(cls, _id):
        return (cls.query.filter_by(survey_id=_id).first())
