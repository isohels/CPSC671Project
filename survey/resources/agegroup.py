from flask_restful import Resource, reqparse
from models.agegroup import AgeGroupModel
from models.surveyagegroups import SurveyAgeGroupModel


class AgeGroupList(Resource):
    def get(self):
        return{'AgeGroup': list(map(lambda x:x.json(), AgeGroupModel.query.all()))}

class SurveyAgeGroupList(Resource):
    def get(self):
        return {"data":list(map(lambda  x: x.json(),SurveyAgeGroupModel.query.all()))}