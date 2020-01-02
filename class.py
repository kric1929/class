class Main:
    food = 'hungry'
    voice = 'silence'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight   # kg

    def feed(self):
        self.food = 'fed'


class Milking:
    milk = 'not milked'

    def to_milk(self):
        self.milk = 'milked'


class Cut:
    haircut = 'not trimmed'

    def shear(self):
        self.haircut = 'trimmed'


class Egg:
    eggs = 0

    def collect_eggs(self, eggs):
        self.eggs += eggs


class Goose(Main, Egg):

    def speak(self):
        self.voice = 'ga-ga ga-ga'


class Cow(Main, Milking):

    def speak(self):
        self.voice = 'moooooo'


class Sheep(Main, Cut):

    def speak(self):
        self.voice = 'beeeee'


class Chicken(Main, Egg):

    def speak(self):
        self.voice = 'ko-ko-ko'


class Goat(Main, Milking):

    def speak(self):
        self.voice = 'me-e'


class Duck(Main, Egg):

    def speak(self):
        self.voice = 'kra-kra'


goose0 = Goose('Серый', 5)
goose0.feed()
goose0.collect_eggs(1)
goose1 = Goose('Белый', 7)
goose1.feed()
goose1.collect_eggs(1)
cow = Cow('Манька', 500)
cow.feed()
cow.to_milk()
sheep0 = Sheep('Барашек', 90)
sheep0.feed()
sheep0.shear()
sheep1 = Sheep('Кудрявый', 70)
sheep1.feed()
sheep1.shear()
chicken0 = Chicken('Ко-Ко', 1)
chicken0.feed()
chicken0.collect_eggs(2)
chicken1 = Chicken('Кукареку', 2)
chicken1.feed()
chicken1.collect_eggs(3)
goat0 = Goat('Рога', 50)
goat0.feed()
goat0.to_milk()
goat1 = Goat('Копыта', 60)
goat1.feed()
goat1.to_milk()
duck = Duck('Кряква', 3)
duck.feed()
duck.collect_eggs(1)

list_animal = [goose0, goose1, cow, sheep0, sheep1, chicken0, chicken1, goat0, goat1, duck]


def to_weight():
    sum_average = 0
    heavy_animal = list_animal[0]
    for animal in list_animal:
        sum_average += animal.weight
        if heavy_animal.weight < animal.weight:
            heavy_animal = animal
    print(sum_average)
    print(heavy_animal.name)


to_weight()
