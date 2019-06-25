from flask import make_response
from flask import request
from flask_restplus import Namespace, Resource
import os

api = Namespace('showimg', description='showimg', ordered=True, validate=True)

@api.route('/<string:filename>')
class ShowPhoto(Resource):
    def get(self,filename):
        if request.method == 'GET':
            if filename is None:
                pass
            else:
                #logger.debug('filename is %s' % filename)
               
                image_data = open(os.path.abspath('.')+ '\\file_uploads\\'+  filename, "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/png'
                return response
        else:
            return 'response'
        #  print(filename)
        #  return  filename

