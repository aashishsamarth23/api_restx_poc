from flask_restx import Api, Resource, Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_restx import fields




api = Api()
ns = Namespace("without_id")
ns1 = Namespace("with_id")