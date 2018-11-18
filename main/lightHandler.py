import lights
import time

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
        print("LightHandler:\n\tInit done")


    def setAmbientLight(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        for i in self.lightingKeys:
            if not i == self.stripKey:
                self.lightController.setLightColour(i, r, b, g)
                self.lightController.setLightBrightness(i, brightness)

    def setStandUpLight(self):
        self.lightController.setLightColour(self.stripKey, 255, 50, 12, 100)


    def setDrinkingLight(self):
        self.lightController.setLightColour(self.stripKey, 102, 153, 204, 10 * 5)
        self.lightController.setLightBrightness(self.stripKey,200)

    def resetStandUpLight(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        self.lightController.setLightColour(self.stripKey, r, b, g, 10 * 5)
        self.lightController.setLightBrightness(self.stripKey, brightness)

    def resetDrinkLight(self, ambientValues):
        rgb = ambientValues[0]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        brightness = ambientValues[1]
        self.lightController.setLightColour(self.stripKey, r, b, g, 50)
        self.lightController.setLightBrightness(self.stripKey, brightness)

    def startAll(self):
        for i in self.lightingKeys:
            self.lightController.setLightOn(i, 20)

    # Schaltet alle Lampen aus
    def terminateAll(self):
        for i in self.lightingKeys:
            self.lightController.setLightOff(i)

        # LED Strip ausschalten
        if (self.stripKey >= 0):
            self.lightController.setLightOff(self.stripKey)

    def fadeLighting(self, r, g, b, ):
        pass


    def toggleLightDelay(self, delay=1):
        print(self.lightingKeys)
        for i in self.lightingKeys:
            self.lightController.toggleLight(i)
            time.sleep(delay)

