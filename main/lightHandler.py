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



    def setDrinkingLight(self):
        self.lightController.setLightColour("7", 0, 0, 230, 1800)

    def fadeLighting(self, r, g, b, ):
        pass