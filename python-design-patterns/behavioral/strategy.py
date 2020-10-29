from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def AlgorithmInterface(self):
        pass

class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print('Called ConcreteStrategyA.AlgorithmInterface()')

class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print('Called ConcreteStrategyB.AlgorithmInterface()')

class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print('Called ConcreteStrategyC.AlgorithmInterface()')

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def ContextInterface(self):
        self._strategy.AlgorithmInterface()


cA  = Context(ConcreteStrategyA())
cB  = Context(ConcreteStrategyB())
cC  = Context(ConcreteStrategyC())
cA.ContextInterface()
cB.ContextInterface()
cC.ContextInterface()
        