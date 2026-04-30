
class vehicle():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def start(self):
        print(f"{self.name} started...")

    def stop(self):
        print(f"{self.name} stopped...")

class car(vehicle):
    def __init__(self, name,capacity,color):
        super().__init__(name, capacity)
        self.color = color

    def getCarColor(self):
        return self.color


car1 = car("Carla",100,"red")
print(f"{car1.name} car color is {car1.getCarColor()}")
car1.start()
car1.stop()
