from flask_restplus import Api
from .textInput import api as text

api = Api(doc='/doc')
api.add_namespace(text, path='/text')


