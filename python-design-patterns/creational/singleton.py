class Singleton:
    __instance = None

    class __Singleton:
        def getUniqueId(self):
            return str(self) + ',id='+str(id(self))

    def __new__(self):
        if Singleton.__instance is None:
             Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance

s = Singleton() 
print(s)

s1 = Singleton()
print(s1.getUniqueId())

s2 = Singleton()
print(s2.getUniqueId())
