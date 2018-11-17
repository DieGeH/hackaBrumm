import time
from datetime import datetime
#   The purpose of the following code is to calculate the ideal value for our ambient light and to figure out if
#   a signal needs to be sent

class Controller:
    def __init__(self):
        self.starttime = datetime.now()
        self.runtime = 0
        self.daytime = 0

    def evaluateSignal(self):
        self.daytime = datetime.now()
        diffInSecs = (self.daytime - self.starttime).total_seconds()
        if 5 < diffInSecs < 10:
            self.resetStartTime()
            print("here")
            return 1
        if diffInMins % 120 == 0:
            return 2
        return 0

    def calculateAmbientLight(self):
        # weiss mit hoechster Intensitaet
        red = 255
        green = 255
        blue = 255
        self.daytime = datetime.now()
        workdurationSecs = (self.daytime-self.starttime).total_seconds()
        if 50 <= workdurationSecs <= (50 + 60):
            blue = int(-(55/(60)) * workdurationSecs + 255)
        ambientRGB = (red, green, blue)
        ambientBrightness = 255
        return [ambientRGB, ambientBrightness]

    def resetStartTime(self):
        self.starttime = datetime.now()
