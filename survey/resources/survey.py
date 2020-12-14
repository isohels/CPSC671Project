from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.survey import SurveyModel
from models.surveylocation import SurveyLocationModel
from models.surveyagegroups import SurveyAgeGroupModel
from models.question import QuestionModel
from models.user import UserModel

class Survey(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('survey_name',
                        type=str,
                        required=True,
                        help="survey_name is not found")
    parser.add_argument('questions',
                        type=dict,
                        required=True,
                        help="Every survey should suppy its questions")

    def post(self, username):
        print("creating survey : "+str(username))
        data = Survey.parser.parse_args()

        user = UserModel.find_by_username(username)
        if user is None:
            return {"message":"Invalid User!"}, 404


        survey = SurveyModel(data.survey_name, user.id)
        try:
            survey.save_to_db()
            survey_id = survey.survey_id
            print(survey.json())
        except:
            return{"message":"An error occured while creating the survey"}, 500

        print("storing question")
        questions = data.questions
        for item in questions['data']:
            q_str = item['question_description']

            question = QuestionModel(survey_id,q_str,0)
            try:
                question.save_to_db()
                print(question.json())
            except:
                return{"message": "An error occured while storing the question"},500

        return {"message":"data saved successfully"}


class SurveyList(Resource):
    def get(self):
        return{'surveys': list(map(lambda x: x.json(), SurveyModel.query.all()))}
    
class SurveyListByUsername(Resource):
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user is None:
            return {"message":"Invalid User!"}, 404
        return{'surveys': list(map(lambda x: x.json(), SurveyModel.query.filter_by(user_id = user.id)))}


class UpdateSurvey(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('survey_name',
                        type=str,
                        required=True,
                        help="Every survey is associated with a user")
    parser.add_argument('questions',
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



    def post(self, survey_id):
        print("update survey post request : "+str(survey_id))
        data = UpdateSurvey.parser.parse_args()
        
        survey = SurveyModel.find_by_id(survey_id)
        if survey is None:
            return {"message ":"Invalid survey id didn't found!"}, 404

        print("storing survey location : "+str(data.location_id))
        print(survey.json())
        location = SurveyLocationModel(survey.survey_id,data.location_id)
        try:
            location.save_to_db()
            print(location.json())
        except:
            return{"message":"An error occured while storing the location"},500


        print("storing survey age group")
        agegroup = SurveyAgeGroupModel(survey.survey_id,data.age_group_id)
        try:
            agegroup.save_to_db()
            print(agegroup.json())
        except:
            return{"message": "An error occured while storing the location"},500

        print("storing question")
        questions = data.questions
        for item in questions['data']:
            question = QuestionModel.find_by_id(item["question_id"])
            if question is None:
                 return {"message ":"Invalid question id didn't found!"}, 404
            q_score = question.score
            q_score+=item["score"]
            question.score = q_score
            try:
                question.save_to_db()
            except:
                return{"message": "An error occured while storing the question"},500
        return {"message":"data updated successfully"}