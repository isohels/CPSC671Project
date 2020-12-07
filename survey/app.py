from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.survey import Survey, SurveyList
from resources.question import QuestionList
from resources.agegroup import AgeGroupList
from resources.location import LocationList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(UserRegister, '/register')
api.add_resource(Survey, '/survey/<string:survey_name>')
api.add_resource(SurveyList, '/surveys')
api.add_resource(QuestionList, '/questions')
api.add_resource(AgeGroupList,'/agegroup')
api.add_resource(LocationList,'/location')




if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
