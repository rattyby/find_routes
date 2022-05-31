# if __name__ == '__main__':
#     pass

class C():
    def __init__(self) -> None:
        self._x = 1
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value
    
    def delx(self):
        del self._x
    
    x = property(getx, setx, delx)

c = C()
c.x = 5
print(c.x)