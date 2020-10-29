from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def Request(self):
        pass

class RealSubject(Subject):
    def Request(self):
        print('Called RealSubject.Request()')

class Proxy(Subject):
    _realSubject = None
    def Request(self):
        #use lazy initialization
        if(self._realSubject == None):
           self._realSubject = RealSubject()
        self._realSubject.Request()

class Client:
    def __init__(self, subject: Subject):
        self._proxySubject = subject

    def ProxyRequest(self):
        self._proxySubject.Request()

c = Client(Proxy())
c.ProxyRequest()
