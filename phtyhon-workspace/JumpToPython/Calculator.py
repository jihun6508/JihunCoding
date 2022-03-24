from statistics import mean

class Calculator():
    def __init__(self, list):
        self.list = list
        
    def sum(self):
        return sum(self.list)
    def avg(self):
        return mean(self.list)
    
ca1 = Calculator([1,2,3,4,5])
print(ca1.sum())
print(ca1.avg())