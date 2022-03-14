from xml.dom.minidom import Document
from flask import request
from mongoengine import StringField, IntField


class Item(Document):

    name = StringField(requerid=True)
    sell_in = IntField()
    quality = IntField()

