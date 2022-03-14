from domain.types import types
from .types import *


# Enum
class Itemizer:
    ITEM_OBJ = {
        "Sulfuras, Hand of Ragnaros": types.Sulfuras,
        "Aged Brie": types.AgedBrie,
        "Backstage passes to a TAFKAL80ETC concert": types.Backstage,
        "Conjured Mana Cake": types.Conjured,
        "+5 Dexterity Vest": types.Conjured,
    }

    @classmethod
    def get(cls, name: str, sell_in: int, quality: int) -> types.NormalItem:
        if name in cls.ITEM_OBJ:
            return cls.ITEM_OBJ[name](name, sell_in, quality)
        return types.NormalItem(name, sell_in, quality)


# Código de: https://github.com/dfleta/flask-rest-ci-boilerplate
class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            item.update_quality()

    def get_items(self) -> list:
        return self.items


# Part
    @staticmethod
    def get_item_typeof(name: str, sell_in: int, quality: int, **kwargs) -> types.NormalItem:
        return Itemizer.get(name, sell_in, quality)

    @classmethod
    def get_items_typeof(cls, raw_items: list[dict]) -> list[types.NormalItem]:
        items = []
        for raw_item in raw_items:
            items.append(cls.get_item_typeof(**raw_item))
        return items