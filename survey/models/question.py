from db import db



class QuestionModel(db.Model):
    __tablename__="Questions"

    question_id = db.Column(db.Integer, primary_key=True)
    question_description = db.Column(db.String(512))
    survey_id = db.Column(db.Integer,db.ForeignKey('surveys.survey_id'))
    score = db.Column(db.Float(precision=2))

    # questions = db.relationship('SurveyModel', lazy= 'dynamic')

    def __init__(self, survey_id,question_description, score):
        self.survey_id = survey_id
        self.question_description = question_description
        self.score = score

    def json(self):
        return {'id':self.question_id,'question':self.question_description,'score':self.score,"survey_id":self.survey_id}

    @classmethod
    def find_by_name(cls,question_description):
        return cls.query.filter_by(question_description=question_description).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(question_id=_id).first()

    @classmethod
    def find_by_survey_id(cls, _id):
        return (cls.query.filter_by(survey_id=_id).all())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
