class ParkingSpace(object):
    """
    This is a base class for parking space
    """

    def __init__(self, parkingSize, parkingType, parkingLevel):
        self.parkingSize = parkingSize
        self.parkingType = parkingType
        self.parkingLevel = parkingLevel


    def getParkingSize(self):
        return self.parkingSize

    def getParkingType(self):
        return self.parkingType

    def getParkingLevel(self):
        return self.parkingLevel



