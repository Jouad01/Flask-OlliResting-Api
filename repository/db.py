import imp
from domain import types


class DB():
    inventario = [[["+5 Dexterity Vest", 10, 20],
                ["Aged Brie", 2, 0],
                ["Elixir of the Mongoose", 5, 7],
                ["Sulfuras, Hand of Ragnaros", 0, 80],
                ["Sulfuras, Hand of Ragnaros", -1, 80],
                ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                ["Backstage passes to a TAFKAL80ETC concert", 5, 49], ]]

    objects = [AgedBrie("Aged Brie", 2, 0), NormalItem(
        "Elixir of the Mongoose", 5, 7)]

    @classmethod
    def get_item(cls, item):
        items = cls.inventario
        return [item for item in items if item[0] == name][0]

    @classmethod
    def get_objects(cls, name):
        items = cls.objects
        return [item for item in items if item.name == name][0]

        objetos = [AgedBrie("Aged Brie", 2, 0),
                   NormalItem("Elixir of the Mongoose", 5, 7)]

  #  @classmethod
  #   def get_item(cls, name):
  #       print(name)
  #       items = cls.inventario
  #       for item in items:
#          if item[0] == name:
  #               return item
  #       return None

  #   @classmethod
  #   def get_objeto(cls, name):
  #       items = cls.objetos
   #      for item in items:
   #          if item.name == name:
   #              return item
   #      return None
