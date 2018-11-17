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


    def setAmbientLight(self):
        # TEST: Licht an
        for i in self.lightingKeys:
            self.lightController.setLightOn(i)

