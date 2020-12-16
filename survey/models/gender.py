from db import db

class GenderModel(db.Model):
    __tablename__ = 'genders'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(80))

    def __init__(self,gender):
        self.gender = gender

    def json(self):
        return {"gender":self.gender,"id":self.id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class SurveyGenderModel(db.Model):
    __tablename__ = 'sruveygenders'

    id = db.Column(db.Integer, primary_key=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.survey_id'))

    def __init__(self,gender_id,survey_id):
        self.gender_id = gender_id
        self.survey_id = survey_id

    def json(self):
        return {"gender_id":self.gender_id,"sruvey_id":self.survey_id,"id":self.id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
