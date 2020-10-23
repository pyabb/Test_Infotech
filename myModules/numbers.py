class numbers:
    def __init__(self, listNumber):
        self.listNumber = listNumber
    
    def sumNumbers(self):
        res = 0
        count = 0
        for i in self.listNumber:
            if count < 5:
                res = res + i
                count += 1
        return res
        