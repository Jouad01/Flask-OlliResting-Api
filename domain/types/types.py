LEGENDARY_QUALITY = 80
# TEN = 10
# FIVE = 5
# MAX_QUALITY = 50
# MIN_QUALITY = 0


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        # Devuelve, no imprime, algo como toString pero en Python
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):  # Añadir clase NormalItem con la que el resto conectan
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_sell_in(self):
        self.sell_in -= 1 

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -1
        elif self.sell_in < 0:
            quality_increase = -2
        self.quality += quality_increase
        if self.quality < 0:
            self.quality = 0
        return self.quality


class Updateable:  
    def update_quality(self):
        # Busca pero pasa del objeto
        pass


class AgedBrie(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in >= 0:
            quality_increase = 1
        elif self.sell_in < 0:
            quality_increase = 2
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality

class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        assert self.quality == LEGENDARY_QUALITY, "quality de %s distinta de 80" % self.__class__.__name__
        pass

class Backstage(NormalItem):

    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 10:
            quality_increase = 1
        elif self.sell_in > 5:
            quality_increase = 2
        elif self.sell_in > 0:
            quality_increase = 3
        elif self.sell_in == 0:
            quality_increase = - self.quality
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality

class Conjured(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -2
        elif self.sell_in < 0:
            quality_increase = -4
        self.quality += quality_increase # La calidad no será negativa
        if self.quality < 0:  
            self.quality = 0
        return self.quality