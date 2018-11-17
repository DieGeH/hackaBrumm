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
        '''
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(str(self.startTime), fmt)
        d2 = datetime.strptime(str(self.daytime), fmt)

        # Convert to Unix timestamp
        d1_ts = time.mktime(d1.timetuple())
        d2_ts = time.mktime(d2.timetuple())

        diffInSecs = int(d2_ts - d1_ts)
        '''
        diffInSecs = (self.daytime - self.starttime).total_seconds()
        diffInMins = (self.daytime - self.starttime).total_seconds()/60
        print(diffInSecs)
        if diffInSecs%(2*60) <= 10:
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
        if 50 <= workdurationSecs <= (50 + 3 * 3600):
            blue = int(-(55/3) * workdurationSecs + 255)
        ambientRGB = (red, green, blue)
        ambientBrightness = 255
        return [ambientRGB, ambientBrightness]

