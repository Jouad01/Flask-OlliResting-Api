from email import message
import resource
from attr import field
from flask_restful import fields, marshal_with, abort


class Service():

    resource_fields = {
        'name': fields.String,
        'sell_in': fields.Integer,
        'quality': fields.Integer
    }
    
    @staticmethod
    
    def get_item(name):
        if not name:
            abort(404, message="Introduzca el nombre del objeto")
        item = DB.get_item(name)
        if not item:
            abort(404, message="El objeto no existe".format(name))

        return {'name': item[0], 'sell_in': item[1], 'quality': item[2]}

    @staticmethod
    @marshal_with(resource_fields)

    def get_objeto(name):
        if not name:
            abort(404, message="Introduzca el nombre del objeto")
        item = DB.get_objeto(name)
        if not item:
            abort(404, message="El objeto no existe".format(name))
        
        return item
        
    