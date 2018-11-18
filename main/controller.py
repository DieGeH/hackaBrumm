import time
import datetime

#   The purpose of the following code is to calculate the ideal value for our ambient light and to figure out if
#   a signal needs to be sent

class Controller:
    def __init__(self):
        self.starttime = datetime.datetime.now()
        self.lastStandUp = datetime.datetime.now()
        self.lastDrink = datetime.datetime.now()
        self.runtime = 0
        self.daytime = 0

        self.thresholdStandUp = None
        self.thresholdDrink = None

    def evaluateSignal(self):
        self.daytime = datetime.datetime.now()
        diffInSecsStandup = int((self.daytime - self.lastStandUp).total_seconds())
        diffInSecsDrink = int((self.daytime - self.lastDrink).total_seconds())

        if diffInSecsStandup == 10:
            self.lastStandUp = datetime.datetime.now()
            print("stand up")
            return 1
        if diffInSecsDrink == 150:
            self.lastDrink = datetime.datetime.now()
            print("drink")
            return 2
        return 0

    def calculateAmbientLight(self):
        # weiss mit hoechster Intensitaet
        red = 255
        green = 255
        blue = 255
        self.daytime = datetime.datetime.now()
        workdurationSecs = (self.daytime-self.starttime).total_seconds()
        ambientRGB = (red, green, blue)
        ambientBrightness = 255
        return [ambientRGB, ambientBrightness]

    def resetStartTime(self):
        self.starttime = datetime.datetime.now()


    def setThresholdStandUp(self, duration):
        #Input: duration in seconds
        self.thresholdStandUp = datetime.datetime.now() + datetime.timedelta(0, duration)


    def setThresholdDrink(self, duration):
        #Input: duration in seconds
        self.thresholdDrink = datetime.datetime.now() + datetime.timedelta(0, duration)


    def isTerminateStandUp(self):
        return datetime.datetime.now() >= self.thresholdStandUp

    def isTerminateDrink(self):
        return datetime.datetime.now() >= self.thresholdDrink
