from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.survey import Survey, SurveyList, UpdateSurvey, SurveyListByUsername
from resources.question import QuestionList
from resources.agegroup import AgeGroupList, SurveyAgeGroupList
from resources.location import LocationList,SurveyLocationList
from resources.retrieve import Retrieve
from models.location import LocationModel
from models.agegroup import AgeGroupModel
from resources.user import UserLogin
from models.gender import GenderModel
from resources.gender import GenderList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

    g1 = ["Male","Female","Other"]
    for i in range(0,len(g1)):
        loc = GenderModel(g1[i])
        db.session.add(loc)
        db.session.commit()

    l1 = ["Alberta","British Columbia","Manitoba","New Brunswick","Ontario","Quebec","Other"]
    for i in range(0,len(l1)):
        loc = LocationModel(l1[i])
        db.session.add(loc)
        db.session.commit()

    a1 = ["less than 20", "20 - 40","41 - 60","greater than 60"]
    for i in range(0,len(a1)):
        age = AgeGroupModel(a1[i])
        db.session.add(age)
        db.session.commit()






jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin,'/login')

api.add_resource(AgeGroupList,'/agegroups')
api.add_resource(LocationList,'/locations')

api.add_resource(GenderList,'/genders')

api.add_resource(Survey, '/create_survey/<string:username>')
api.add_resource(SurveyList, '/surveys')
api.add_resource(SurveyListByUsername, '/surveys/<string:username>')
api.add_resource(QuestionList, '/questions')

api.add_resource(Retrieve, '/survey/<int:survey_id>')
api.add_resource(UpdateSurvey,'/submit_survey/<int:survey_id>')

api.add_resource(SurveyAgeGroupList,'/surveyagegroups')
api.add_resource(SurveyLocationList,'/surveylocations')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
