class Column:
    def __init__(self, name, values, type):
        self.name = name
        self.values = values
        self.type = type

    def __str__(self):
        return f"{self.name}, {self.type}"
    
    def getValues(self):
        return self.values
    
    def setType(self, type):
        self.type = type