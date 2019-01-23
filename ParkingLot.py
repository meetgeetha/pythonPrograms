from ParkingSpace import ParkingSpace
from Car import Car
import json

class ParkingLot(object):
    """
    This is a base class for parking lot
    See the json file to see the data structure used for parking lot creation
    """

    def __init__(self, size=None, type=None, level=None, slots=None):
        self.parkingDict={}

    def addLot(self,ps, num):
        self.parkingDict[ps]=num

    def parkCar(self, car, level):
        for keys,values in self.parkingDict.items():
            if keys.getParkingSize() == car.getCarSize() and keys.getParkingType() == car.getCarType() and keys.getParkingLevel() == level:

                if values > 0:
                    print("Car can be parked")
                    values -= 1
                    self.parkingDict[keys]= values
                    print("In this level we have {} spots left!".format(values))
                else:
                    print("Car cannot be parked, we don't have space in this level")


pl = ParkingLot()


with open('parkinglot.json') as data_file:
    parkingData = json.load(data_file)

for keys in parkingData:
    pl.addLot(ParkingSpace(parkingData[keys]['size'], parkingData[keys]['type'], parkingData[keys]['level']), parkingData[keys]['count'])

car = Car("SMALL", "REGULAR")
pl.parkCar(car, "First")
pl.parkCar(car, "First")
pl.parkCar(car, "First")


