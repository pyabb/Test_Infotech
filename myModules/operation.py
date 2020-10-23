class operation:
    def __init__(self, listNumber):
        self.listNumber = listNumber
    
    def suma(self):
        res = 0
        for i in self.listNumber:
            res += i
        return res

    def multip(self):
        res = 1
        for i in self.listNumber:
            res *= i
        return res