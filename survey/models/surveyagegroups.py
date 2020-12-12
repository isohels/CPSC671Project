from db import db

class SurveyAgeGroupModel(db.Model):
    __tablename__ = 'survey_agegroups'

    id = db.Column(db.Integer,primary_key = True)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.survey_id'))
    agegroup_id = db.Column(db.Integer,db.ForeignKey('agegroups.id'))
    # survey = db.relationship("SurveyModel")
    # agegroup = db.relationship("AgeGroupModel")

    # locations = db.relationship('SurveyModel', lazy= 'dynamic')

    def __init__(self,survey_id,agegroup_id):
        self.survey_id = survey_id
        self.agegroup_id = agegroup_id

    def json(self):
        return {"survey_id":self.survey_id,"agegroup_id":self.agegroup_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
