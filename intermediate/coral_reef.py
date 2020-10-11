class Coral:
    def community(self):
        print("Coral livesi n a community")

class Anemonae:
    def protect_clownfish(self):
        print("The anemonae is protecting the clownfish")

class CoralReef(Coral, Anemonae):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
