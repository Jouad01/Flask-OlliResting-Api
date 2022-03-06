from flask_restful import Resource

class Wellcome(Resource):
    def get(self):
        return {"Hola": "Ollivanders"}