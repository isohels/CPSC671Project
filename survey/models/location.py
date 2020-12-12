from db import db

class LocationModel(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    location_description = db.Column(db.String(80))

    # locations = db.relationship('SurveyModel', lazy= 'dynamic')

    def __init__(self,location_description):
        self.location_description = location_description

    def json(self):
        return {"location":self.location_description}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
