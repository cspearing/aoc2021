class Window:
    

    def __init__(self, limit):
        self.maxSize = limit
        self.size = 0
        self.values = []
    
    def add(self, value):
        if self.size < self.maxSize:
            self.values.append(value)
            self.size += 1

    def full(self):
        return self.size == self.maxSize

    def total(self):
        return sum(self.values)
            