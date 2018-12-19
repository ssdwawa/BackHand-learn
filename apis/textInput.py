from flask import jsonify, request, Response
from models import Content
from flask_restplus import Namespace, Resource
from config import db, photo_test

api = Namespace('TEXT RICH', description='TEXT RICH', ordered=True, validate=True)

@api.route('/submit')
class Log(Resource):
    def post(self):
        word = request.form.get('content')
        content = Content(
            Content=word
        )
        db.session.add(content)
        db.session.commit()
        return 'ojbk'
    def get(self):
        return 'test'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@api.route("/ImageUpdate")
class GetImage(Resource):
    def post(self):
        file = list(request.files.to_dict(flat=False).values())[0][0]
        print(file)
        if file == None:
            result = r"error|未成功获取文件，上传失败"
            res = Response(result)
            res.headers["ContentType"] = "text/html"
            res.headers["Charset"] = "utf-8"
            return res
        else:
            if file and allowed_file(file.filename):
                filename = photo_test.save(file)
                file_url = photo_test.url(filename)
                res = {
                    "errno": 0,
                    "data": [
                        file_url,
                    ]
                }
                res["ContentType"] = "text/html"
                res["Charset"] = "utf-8"
                return res


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
