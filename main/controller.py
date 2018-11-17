#   The purpose of the following code is to calculate the ideal value for our ambient light and to figure out if
#   a signal needs to be sent

class Controller:
    def __init__(self):
        self.startTime = 0
        self.runTime = 0
        self.daytime = 0

    def evlauateSignal(self):
        return 0

    def calculateAmbientLight(self):
        # weiß mit höchster Intensität
        red = 255
        green = 255
        blue = 255
        ambientRGB = (red, green, blue)
        ambientBrightness = 255
        return ambientRGB, ambientBrightness

