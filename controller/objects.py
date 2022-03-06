from flask_restful import Resource
from services.services import Service

class Objeto(Resource):
    
    def get(self, name):
        return Service.get_objeto(name), 200  #Ping?¿