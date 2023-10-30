class Passenger:
    def __init__(self, place):
        self.place = place
    
    def getPlace(self):
        return self.place

class Taxi:
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        return f"Taxi {self.id}"