class animal:
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):
        print("barks")

d=dog()
d.sound()