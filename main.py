from taxi import Taxi
from taxi_company import TaxiCompany
from place import Place
from passenger import Passenger
from taxi_manager import TaxiManager

place1 = Place("Yunusobod ko'cha 123", "A okrugi", "Sadacha mahallasi")
passenger1 = Passenger(place1)

taxi1 = Taxi(1)
taxi2 = Taxi(2)
taxi3 = Taxi(3)

company = TaxiCompany()
company.addTaxi(taxi1)
company.addTaxi(taxi2)
company.addTaxi(taxi3)

manager = TaxiManager(company)
taxi_assigned = manager.callTaxi(passenger1)

if taxi_assigned:
    print(f"Belgilangan yo'lovchi {str(taxi_assigned)}")
else:
    print("Mavjud taksilar yo'q")

lost_trips_count = manager.getLostTrips()
print(f"Yo'qotilgan sayohatlar: {lost_trips_count}")