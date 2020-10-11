class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids="false"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    @staticmethod
    def swim():
        print("The fish is swimming.")

    @staticmethod
    def swim_backwards():
        print("The fish can swim backwards.")


class Trout(Fish):
    def __init__(self, water="fresh water"):
        self.water = water
        super().__init__(self)


class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish " + self.first_name + " is coexisting with anemone")

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards")


terry = Trout()
terry.first_name = "Terry"
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
print(terry.water)

casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
