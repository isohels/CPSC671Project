from db import db


class SurveyModel(db.Model):
    __tablename__ = "surveys"

    survey_id = db.Column(db.Integer, primary_key=True)
    survey_name = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    survey = db.relationship('UserModel')


    def __init__(self,survey_name,user_id):
        self.survey_name = survey_name
        self.user_id = user_id


    def json(self):
        return{'name': self.survey_name}


    @classmethod
    def find_by_name(cls, survey_name):
        return cls.query.filter_by(survey_name=survey_name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
