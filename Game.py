class Game():

    #game class to hold the name and description of each game
    def __init__(self, name = '', description = ''):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description