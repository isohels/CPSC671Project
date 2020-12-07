from flask_restful import Resource, reqparse
from models.agegroup import AgeGroupModel


class AgeGroupList(Resource):
    def get(self):
        return{'AgeGroup': list(map(lambda x:x.json(), AgeGroupModel.query.all()))}
