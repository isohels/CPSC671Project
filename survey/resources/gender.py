from flask_restful import Resource, reqparse
from models.gender import GenderModel


class GenderList(Resource):
    def get(self):
        return{'gender': list(map(lambda x:x.json(), GenderModel.query.all()))}