from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.survey import SurveyModel
from models.surveylocation import SurveyLocationModel
from models.surveyagegroups import SurveyAgeGroupModel
from models.question import QuestionModel

class Survey(Resource):
    # data = parser.parse_args()
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="Every survey is associated with a user")
    parser.add_argument('question_description',
                        type=dict,
                        required=True,
                        help="Every survey should suppy its questions")
    parser.add_argument('location_id',
                        type=int,
                        required=True,
                        help="Surveyor should send location")
    parser.add_argument('age_group_id',
                        type=int,
                        required=True,
                        help="Surveyor should send agegroup")




    def get(self, user_id):
        survey = SurveyModel.find_by_name(survey_name)
        if survey:
            return survey.json()

        return {'message': 'Survey not found'}, 404

    def post(self, survey_name):
        data = Survey.parser.parse_args()


        survey = SurveyModel(survey_name, data['user_id'])
        try:
            survey.save_to_db()
            survey_id = survey.survey_id
            print(survey.json())
        except:
            return{"message":"An error occured while creating the survey"}, 500


        location = SurveyLocationModel(survey_id,data.location_id)
        try:
            location.save_to_db()
            print(location.json())
        except:
            return{"message":"An error occured while storing the location"},500


        agegroup = SurveyAgeGroupModel(survey_id,data.age_group_id)
        try:
            agegroup.save_to_db()
            print(agegroup.json())
        except:
            return{"message": "An error occured while storing the location"},500


        questions = data.question_description
        for item in questions['data']:
            q_str = item['question']
            print(q_str)
            question = QuestionModel(survey_id,q_str,0)
            try:
                question.save_to_db()
                # print(question.json())
                # print(str(question.id))
            except:
                return{"message": "An error occured while storing the question"},500

        return {"message":"data saved successfully"}


class SurveyList(Resource):
    def get(self):
        return{'surveys': list(map(lambda x: x.json(), SurveyModel.query.all()))}
