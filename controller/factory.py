from unicodedata import name
from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.objects import Objeto
from controller.wellcome import Wellcome

def creacion_app():
    app = Flask(__name__)
    
    api = Api(app, catch_all_404s=True)

    api.add_resource(Wellcome, "/")
    api.add_resource(Items, "/")
    api.add_resource(Objeto, "/")

    return app

if __name__ == '__main__':
    app = creacion_app()
    app.run(debug=True)