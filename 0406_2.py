# import random

# listA = list(range(1, 10))
# listA = listA.sort()
# print(listA)

# class miner:
#     def __init__(self, mineral):
#         self.__mineral = mineral
#     def getMineral(self): return self.__mineral
#     def setMineral(self, mineral): self.__mineral = mineral
# SCV = miner(100)
# print(SCV.getMineral())
# print(SCV.setMineral(200))
# print(SCV.getMineral())

class BankAccount:
    def __init__(self, deposit):
        self.__deposit = deposit
    
    @property
    def deposit(self): return self.__deposit
    @deposit.setter
    def deposit(self, m): 
        self.__deposit = m

    def withdraw(self, m): 
        print(m,'만큼 출금')
        self.__deposit -= m
        


b = BankAccount(100)
print(b.deposit)
b.deposit = 200
print(b.deposit)
b.withdraw(5)
print(b.deposit)