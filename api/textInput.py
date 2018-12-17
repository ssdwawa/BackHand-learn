from flask import Blueprint,jsonify,request
from models import Content , db

api = Blueprint('api', __name__)

@api.route('/log')
def log():
    return jsonify('is log')

@api.route('/submit' ,  methods=['POST'])
def insert():
    word = request.form.get('content')
    content = Content(1,word)
    print(content)

