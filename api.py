from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.wellcome import Wellcome 
from controller.objeto import Objeto


app = Flask(__name__)

# API REST
api = Api(app, catch_all_404s=True)

api.add_resource(Wellcome, '/')
api.add_resource(Items, '/item/<name>')
api.add_resource(Objeto, '/objeto/<name>')


if __name__ == '__main__':
    app.run(debug=True)