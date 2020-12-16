from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.survey import SurveyModel
from models.surveylocation import SurveyLocationModel
from models.surveyagegroups import SurveyAgeGroupModel
from models.question import QuestionModel
from models.location import LocationModel
from models.agegroup import AgeGroupModel
from models.gender import GenderModel, SurveyGenderModel
from db import db
import sqlite3


class Retrieve(Resource):

    parser = reqparse.RequestParser()

    def get(self, survey_id):
        print("getting into the request")
        response = {}
        survey = SurveyModel.find_by_id(survey_id)
        if survey is None:
            return {"message":"Can't find the survey!"}, 404
        response["name"] = survey.survey_name
        response["id"] = survey.survey_id

        questions = QuestionModel.query.filter_by(survey_id = survey_id)
        questions_data = []
        for question in questions:
            question_data = {"question_id":question.question_id,"question_description":question.question_description,
                            "score":question.score}
            questions_data.append(question_data)
        
        response["questions"] = questions_data
        survey_location = db.session.query(LocationModel,SurveyLocationModel).outerjoin(SurveyLocationModel,LocationModel.id == SurveyLocationModel.location_id).filter_by(survey_id = survey_id).all()
        # getting data ready for location_survey based on all location where survey id equals to the given
        result = []
        loc_dic = {}
        for location, _ in survey_location:
            if location.id in loc_dic.keys():
                loc_dic[location.id]+=1
            else:
                loc_dic[location.id] = 1
        
        for key in loc_dic:
            result.append({'id':key,"location":loc_dic[key]})
        
        response["location_data"] = result

        # getting data ready for survey age based on all location where survey id equals to the given
        survey_agegroups = db.session.query(AgeGroupModel,SurveyAgeGroupModel).outerjoin(SurveyAgeGroupModel,AgeGroupModel.id == SurveyAgeGroupModel.agegroup_id).filter_by(survey_id = survey_id).all()
        
        result = []
        age_dic = {}
        for agegroup, _ in survey_agegroups:
            if agegroup.id in age_dic.keys():
                age_dic[agegroup.id]+=1
            else:
                age_dic[agegroup.id] = 1
        
        for key in age_dic:
            result.append({'id':key,"description":age_dic[key]})
        response["age_group_data"] = result

        #getting data ready for survey gender based 
        survey_gender = db.session.query(GenderModel,SurveyGenderModel).outerjoin(SurveyGenderModel,GenderModel.id == SurveyGenderModel.gender_id).filter_by(survey_id = survey_id).all()
        print(survey_gender)
        result = []
        gender_dic = {}
        for gender, _ in survey_gender:
            if gender.id in gender_dic.keys():
                gender_dic[gender.id]+=1
            else:
                gender_dic[gender.id] = 1
        print(gender_dic)
        for key in gender_dic:
            result.append({'id':key,"count":gender_dic[key]})
        
        response["gender_data"] = result

        return response
