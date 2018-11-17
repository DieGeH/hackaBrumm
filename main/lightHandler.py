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

        self.connected = True


    def setAmbientLight(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        for i in self.lightingKeys:
            self.lightController.setLightColour(i, r, b, g)
            self.lightController.setLightBrightness(i, brightness)


    # Schaltet alle Lampen aus
    def terminateAll(self):
        for i in self.lightingKeys:
            self.lightController.setLightOff(i)

        # LED Strip ausschalten
        if (stripKey >= 0):
            self.lightController.setLightOff(stripKey)

    def fadeLighting(self, r, g, b, ):
        pass