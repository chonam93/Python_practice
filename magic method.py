class miner:
    def __init__(self, mineral, gas):
        self.mineral = mineral
        self.gas = gas

    def printM(self):
        print(self.mineral)
        print(self.gas)
    
    def __add__(self, other):
        return miner(self.mineral + other.mineral, self.gas + other.gas)

SCV = miner(50, 30)
probe = miner(100, 30)
drone = SCV + probe # SCV.__add__(probe)와 동일
drone.printM()