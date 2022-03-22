import mod_1
class FourCal:
    def __init__(self, a, b):
        self.First = a
        self.Second = b
    def setdata(self,a,b):
        self.First = a
        self.Second = b
    def add (self):
        result = self.First + self.Second
        return result
    def sub (self):
        result = self.First - self.Second
        return result
    def mul (self):
        result = self.First * self.Second
        return result
    def div (self):
        result = self.First / self.Second
        return result
a=FourCal(3,4)

print(a.add())

class MoreFourCal(FourCal):
    def squared(self):
        result = self.First**self.Second
        return result

b = MoreFourCal(4,3)

print(b.sub())
print(b.squared())

class SafeFourCal(FourCal):
    def div(self):
        if self.Second == 0:
            return 0
        else: return self.First/self.Second

c = SafeFourCal(1,0)

print(c.div())
d = mod_1.Math(4)
print(d.solv())