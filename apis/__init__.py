from flask_restplus import Api
from .textInput import api as text
from .imgshow import api as img

api = Api(doc='/doc')
api.add_namespace(text, path='/text')
api.add_namespace(img, path='/img')

