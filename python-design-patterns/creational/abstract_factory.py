from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def CreateProductA(self): 
        pass
    @abstractmethod
    def CreateProductB(self): 
        pass

class ConcreteFactory1(AbstractFactory):
    def CreateProductA(self):
        return ProductA1()

    def CreateProductB(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def CreateProductA(self):
        return ProductA2()

    def CreateProductB(self):
        return ProductB2()

class AbstractProductA: 
        pass
class AbstractProductB: 
    def Interact(self,abstractProduct: AbstractProductA):
        pass

class ProductA1(AbstractProductA): 
        pass
class ProductB1(AbstractProductB): 
    def Interact(self,abstractProduct: AbstractProductA):
        print(self.__class__.__name__ + ' interacts with ' + abstractProduct.__class__.__name__)
        
class ProductA2(AbstractProductA): 
        pass
class ProductB2(AbstractProductB): 
    def Interact(self,abstractProduct: AbstractProductA):
        print(self.__class__.__name__ + ' interacts with ' + abstractProduct.__class__.__name__)
        
class Client:
    def __init__(self,              factory: AbstractFactory):
        self._abstractProductA    = factory.CreateProductA()
        self._abstractProductB    = factory.CreateProductB()
    
    def Run(self):
        self._abstractProductB.Interact(self._abstractProductA)

factory1 = ConcreteFactory1()
client1  = Client(factory1)      
client1.Run()

factory2 = ConcreteFactory2()
client2  = Client(factory2)      
client2.Run()

