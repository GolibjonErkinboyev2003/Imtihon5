class TaxiCompany:
    def __init__(self):
        self.taxis = []
    
    def addTaxi(self, taxi):
        for t in self.taxis:
            if t.id == taxi.id:
                raise Exception("Invalid TaxiName")
        
        self.taxis.append(taxi)
    
    def getAvailable(self):
        return [taxi for taxi in self.taxis if not taxi.isOccupied]