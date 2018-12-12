
class Factorial:

    def __init__(self, n):
        self.n = n
    
    def fac(self):
        assert(self.n >= 0), "Please enter an int greater or equals 0"
        if self.n == 0:
            result = 1
            return result
        multiple, prod = self.n - 1, 1
        
        while multiple >= 1:
            prod = prod * multiple
            multiple = multiple - 1

        result = self.n * prod
        return result

