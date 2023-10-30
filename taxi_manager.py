class TaxiManager:
    def __init__(self, taxi_company):
        self.taxi_company = taxi_company
        self.lost_trips = 0
    
    def callTaxi(self, passenger):
        available_taxis = self.taxi_company.getAvailable()
        
        if len(available_taxis) > 0:
            taxi = available_taxis[0]
            taxi.startTrip(passenger.getPlace())
            return taxi
        else:
            return None
    
    def getLostTrips(self):
        return self.lost_trips