class Car(object):
    """
    This is a class that represents the base car
    """

    def __init__(self, carSize, carType):
        self.carSize = carSize
        self.carType = carType

    def getCarType(self):
        return self.carType

    def getCarSize(self):
        return self.carSize
