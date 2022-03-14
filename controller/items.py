from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import abort, make_response, g
from repository.db import DB
from repository.types.Item import Item
from domain.GildedRose import GildedRose


class Items(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument("name", type=str, required=True)
        self.parser.add_argument("quality", type=int, required=True)
        self.parser.add_argument("sell_in", type=int, required=True)

    def get(self):
        db = db.get_db()
        items = db.query(Item).all()
        return [item.serialized for item in items]

    def post(self):
        args = self.parser.parse_args()
        if isinstance(args['name'], str) and \
                isinstance(args['quality'], int) and \
                isinstance(args['sell_in'], int):
            db = db.get_db()
            item = Item(name=args['name'],
                        quality=args['quality'],
                        sell_in=args['sell_in'])
            db.add(item)  # Se guarda en la base de datos y devuelve 202, cuando se cierra app_context
            return make_response(item.serialized, 202)

        return abort(400)

    class FilterName(Resource):
        def get(self, name: str = None):
            if name:
                db = db.get_db()
                items = db.query(Item).filter_by(name=name).all()
                return [item.serialized for item in items]

    class FilterQuality(Resource):
        def get(self, quality: int = None):
            if quality:
                db = db.get_db()
                items = db.query(Item).filter_by(quality=quality).all()
                return [item.serialized for item in items]

            return abort(400, "'quality' debería ser un número")

    class FilterSellIn(Resource):
        def get(self, sell_in: int = None):
            if sell_in:
                db = db.get_db()
                items = db.query(Item).filter_by(sell_in=sell_in).all()
                return [item.serialized for item in items]

            return abort(400, "'sell_in' debería ser un número")

    class UpdateQuality(Resource):
        def get(self):
            if 'shop' not in g:
                db = db.get_db()
                items = [item.serialized for item in db.query(Item).all()]
                g.shop = GildedRose(GildedRose.get_items_typeof(items))

            g.shop.update_quality()

            return make_response("Updated", 200)