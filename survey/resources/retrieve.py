from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.survey import SurveyModel
from models.surveylocation import SurveyLocationModel
from models.surveyagegroups import SurveyAgeGroupModel
from models.question import QuestionModel
from models.location import LocationModel
from models.agegroup import AgeGroupModel
from db import db


class Retrieve(Resource):

    parser = reqparse.RequestParser()

    def post(self, survey_id):
        mylist = []
        survey = SurveyModel.find_by_id(survey_id)
        mylist.append(survey.json())
        # print(mylist)
        agegroup = SurveyAgeGroupModel.find_by_survey_id(survey_id)
        mylist.append(agegroup.json())
        location = SurveyLocationModel.find_by_survey_id(survey_id)
        mylist.append(location.json())
        question = QuestionModel.find_by_survey_id(survey_id)
        for q in question:
            print(mylist.append(q.json()))
        return(mylist)
