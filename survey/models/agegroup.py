from db import db

class AgeGroupModel(db.Model):
    __tablename__ = 'agegroup'

    id = db.Column(db.Integer, primary_key=True)
    group_description = db.Column(db.String(80))


    def __init__(self,group_description):
        self.group_description = group_description


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
