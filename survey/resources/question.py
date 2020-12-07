from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.question import QuestionModel


class Question(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('question_description',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")





    def post(self, question_description):
        data = Question.parser.parse_args()
        question_description = question_description(name,**data)

        try:
            question_description.save_to_db()
        except:
            return{"message":"An error occured inserting the item."},500

        return question_description.json(),201

class QuestionList(Resource):
    def get(self):
        return{'questions': list(map(lambda x:x.json(), QuestionModel.query.all()))}
