# class miner:
#     totalmineral = 0
#     def __init__(self, mineral):
#         self.mineral = mineral
#         miner.totalmineral += mineral
#     def printMineral(self):
#         print(self.mineral)
#     def miningMineral(self):
#         self.mineral += 10
#         miner.totalmineral += 10

#     @classmethod
#     def printMineral(cls):
#         print(cls.totalmineral)

# SCV = miner(50)
# probe = miner(100)
# miner.printMineral()
# SCV.miningMineral()
# SCV.printMineral()
# probe.printMineral()
# miner.printMineral()
# SCV.miningMineral()
# SCV.printMineral()
# miner.printMineral()
# SCV.miningMineral()
# SCV.printMineral()
# probe.miningMineral()


class miner:
    totalMineral = 0
    totalGas = 0

    def __init__(self, mineral, gas):
        self.mineral = mineral
        miner.totalMineral += mineral
        self.gas = gas
        miner.totalGas += gas

    def printMineral(self):
        print(self.mineral)
        print(self.gas)

    def miningMineral(self):
        self.mineral += 10
        miner.totalMineral += 10

    def miningGas(self):
        self.gas += 5
        miner.totalGas += 5

    @classmethod
    def printMineral(cls):
        print(cls.totalMineral)
        print(cls.totalGas)    

# SCV = miner(50, 100)
# print('처음데이터 ',SCV.gas)
# SCV.miningGas
# print(SCV.totalGas)

SCV = miner(50, 80)
probe = miner(50, 70)
miner.printMineral()
SCV.miningMineral()
SCV.printMineral()
probe.printMineral()
miner.printMineral()
SCV.miningMineral()
SCV.printMineral()
miner.printMineral()
SCV.miningMineral()
SCV.printMineral()
probe.miningMineral()