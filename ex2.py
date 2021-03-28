class Сlothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_square_full(self):
        return str(f'Общая площадь ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь пальто: {self.square_coat}'


class Suit(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь костюма: {self.square_suit}'


coat = Coat(20, 96)
suit = Suit(55, 78)
print(coat)
print(suit)
print(coat.get_square_full)
print(suit.get_square_full)
