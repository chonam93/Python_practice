class miner:
    def __init__(self, mineral, gas):
        self.__mineral = mineral
        self.__gas = gas
    @property
    def mineral(self): return self.__mineral
    @property
    def gas(self): return self.__gas
    @mineral.setter
    def mineral(self, m): self.__mineral = m
    def miningMineral(self, m): self.__mineral += m
    @gas.setter
    def gas(self, g): self.__gas = g
    def miningGas(self, g): self.__gas += g



SCV = miner(100, 50) #miner 클래스에 mineral 100 / gas 50 입력한 SCV 인스턴스 생성
print(SCV.mineral, end=" ") #현재 미네랄 및 가스 출력/ 라인 6과 8참고
print(SCV.gas)
cnt = 0
while cnt < 5: #함수 다섯번 반복
    SCV.miningMineral(10) #설정자 method / 라인 11 / 10만큼 미네랄 증가
    SCV.miningGas(5) #설정자 method / 라인 14 / 5만큼 가스 증가
    print('미네랄: ',SCV.mineral, end=" ")
    print('가스: ', SCV.gas)
    cnt += 1