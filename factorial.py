class Factorial:
    def __init__(self, n):
        self.n = n
    def fac(self):
        if type(self.n) != int or self.n < 0: 
            return "Please enter an int greater or equals 0"
        elif self.n == 0:
            return 1
        multiple, prod = self.n - 1, 1
        while multiple >= 1:
            prod = prod * multiple
            multiple = multiple - 1
        result = self.n * prod
        return result

