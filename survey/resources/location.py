from flask_restful import Resource, reqparse
from models.location import LocationModel
from models.surveylocation import SurveyLocationModel


class LocationList(Resource):
    def get(self):
        return{'Location': list(map(lambda x:x.json(), LocationModel.query.all()))}


class SurveyLocationList(Resource):
    def get(self):
        return {"data":list(map(lambda  x: x.json(),SurveyLocationModel.query.all()))}