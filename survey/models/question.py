from db import db


class QuestionModel(db.Model):
    __tablename__="Questions"

    question_id = db.Column(db.Integer, primary_key=True)
    question_description = db.Column(db.String(80))
    score = db.Column(db.Float(precision=2))


    def __init__(self, question_description, score):
        self.question_description = question_description
        self.score = score

    def json(self):
        return {'question':self.question_description,'score':self.score}

    @classmethod
    def find_by_name(cls,question_description):
        return cls.query.filter_by(question_description=question_description).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
