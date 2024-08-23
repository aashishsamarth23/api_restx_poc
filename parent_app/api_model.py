from extensions import fields
from extensions import api




first_model = api.model('data1', {
    "id": fields.Integer,
    "name": fields.String,
    "course": fields.String
})




second_model = api.model('data2', {
    "id": fields.Integer,
    "course": fields.String,
    "difficulty": fields.String
})




first_input_model = api.model("data1_input", {
    
    "name": fields.String,
    "course": fields.String
})




second_input_model = api.model("data2_input", {
    
    "course": fields.String,
    "difficulty": fields.String
})
