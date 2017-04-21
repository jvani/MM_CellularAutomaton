import random

class SimpleTrafficGenerator():
    def __init__(self, carPerUpdate=1):
        self.queue = 0
        self.carPerUpdate = carPerUpdate

    def generate(self, road):
        randBinList = lambda n: [random.randint(0,1) for b in range(1, n+1)]
        amount = random.choice([0,1,1])
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)


