from extensions import SQLAlchemy
db = SQLAlchemy()




class data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    course = db.Column(db.String(200), nullable = False)



    
class course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    course = db.Column(db.String(100), nullable = False)
    difficulty = db.Column(db.String(200), nullable = False)
