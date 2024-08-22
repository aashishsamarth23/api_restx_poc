from flask import Flask
from flask_restx import Resource, Namespace
from models import db, course, data
from api_model import api, first_model, first_input_model, second_model, second_input_model
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db.init_app(app)
with app.app_context():
    db.create_all()
ns = Namespace("api")
api.init_app(app)
api.add_namespace(ns)
@ns.route('/student')
class HelloWorld(Resource):
    @ns.marshal_list_with(first_model)
    def get(self):
        testdb = data(name = 'some name', course = 'some course')
        db.session.add(testdb)
        db.session.commit()
        check = data.query.all()
        return check
    @ns.marshal_list_with(first_model)
    @ns.expect(first_input_model)
    def post(self):
        course = data(name = ns.payload["name"], course = ns.payload["course"])
        db.session.add(course)
        db.session.commit()
        return course, 201
@ns.route('/courses')
class api_course(Resource):
    @ns.marshal_list_with(second_model)
    def get(self):
        testdb = course(course = 'some name', difficulty = 'easy')
        db.session.add(testdb)
        db.session.commit()
        check = course.query.all()
        return check
    @ns.expect(second_input_model)
    @ns.marshal_list_with(second_model)
    def post(self):
        c = course(course = ns.payload["course"], difficulty = ns.payload["difficulty"])
        db.session.add(c)
        db.session.commit()
        newCheck = course.query.all()
        return newCheck, 201
@ns.route("/student/get_update_delete/<int:id>")
class api_update_delete(Resource):
    @ns.marshal_list_with(first_model)
    def get(self, id):
        test = data.query.get(id)
        return test, 201
    @ns.marshal_list_with(first_model)
    @ns.expect(first_input_model)
    def put(self, id):
        this_course = data.query.get(id)
        this_course.name = ns.payload["name"]
        this_course.course = ns.payload["course"]
        db.session.commit()
        return this_course
    @ns.marshal_list_with(first_model)
    def delete(self, id):
        this_course = data.query.get(id)
        db.session.delete(this_course)
        db.session.commit()
        return {}, 204
if __name__ == '__main__':
    app.run(debug=True, port = 8000)