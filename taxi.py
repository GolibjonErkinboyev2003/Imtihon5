class Taxi:
    def __init__(self, id):
        self.id = id
        self.isOccupied = False
    
    def __str__(self):
        return f"Taxi {self.id}"
    
    def startTrip(self, destination):
        self.isOccupied = True
    
    def endTrip(self):
        self.isOccupied = False
        