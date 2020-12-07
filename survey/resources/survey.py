from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.survey import SurveyModel


class Survey(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="Every survey is associated with a user")





    def get(self, survey_name):
        survey = SurveyModel.find_by_name(survey_name)
        if survey:
            return survey.json()

        return {'message': 'Store not found'}, 404

    def post(self, survey_name):
        data = Survey.parser.parse_args()

        survey = SurveyModel(survey_name, **data)

        try:
            survey.save_to_db()
        except:
            return{"message":"An error occured while creating the store"}, 500

        return survey.json(), 201




class SurveyList(Resource):
    def get(self):
        return{'surveys': list(map(lambda x: x.json(), SurveyModel.query.all()))}
