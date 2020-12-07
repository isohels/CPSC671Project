from flask_restful import Resource, reqparse
from models.location import LocationModel


class LocationList(Resource):
    def get(self):
        return{'Location': list(map(lambda x:x.json(), LocationModel.query.all()))}
