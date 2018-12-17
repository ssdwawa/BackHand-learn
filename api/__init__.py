from flask import Flask
from api.textInput import  api as home_bluePrint

app = Flask(__name__)

app.debug =True

app.register_blueprint(home_bluePrint, url_prefix="/text")

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


if __name__ == '__main__':
    app.run(debug = True)
