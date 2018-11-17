import lights

class LightHandler:

    def __init__(self):
        self.connected = False


    def initState(self):
        # Low-level lights objekt
        self.lightController = lights.Lightse()
        self.lightController.getLights()

        # Hoeher-Level Lampen Objekte
        self.lightingKeys = self.lightController.getLightKeys()
        self.stripKey = self.lightController.getStripKey()

        self.startAll()

        self.connected = True


    def setAmbientLight(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        for i in self.lightingKeys:
            if not i == self.sripKey:
                self.lightController.setLightColour(i, r, b, g)
                self.lightController.setLightBrightness(i, brightness)

    def setStandUpLight(self):
        self.lightController.setLightColour(self.stripKey, 230, 10, 12)


    def setDrinkingLight(self):
        self.lightController.setLightColour(self.stripKey, 0, 0, 230)

    def setStripOnAmbient(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        self.lightController.setLightColour(self.stripKey, r, b, g)
        self.lightController.setLightBrightness(self.stripKey, brightness)

    def startAll(self):
        for i in self.lightingKeys:
            self.lightingKeys.setLightOn(i, 20)

    # Schaltet alle Lampen aus
    def terminateAll(self):
        for i in self.lightingKeys:
            self.lightController.setLightOff(i)

        # LED Strip ausschalten
        if (self.stripKey >= 0):
            self.lightController.setLightOff(self.stripKey)

    def fadeLighting(self, r, g, b, ):
        pass