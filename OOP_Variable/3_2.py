class Cal(object):
    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, v):
        if isinstance(v, int):
            self._v1 = v

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, v):
        if isinstance(v, int):
            self._v2 = v

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2


c1 = Cal(10,10)
print(c1.add()) # 20
print(c1.subtract()) # 0

c1.v1 = 'one' # ignore. v1 is 10
c1.v2 = 30
print(c1.add()) # 40
print(c1.subtract()) # -20
