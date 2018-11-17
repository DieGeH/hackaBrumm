import lights.Lightse


class LightHandler:

    def __init__(self):
        self.connected = False


    def initState(self):
        # Low-level lights objekt
        self.lightController = Lightse()

        # Hoeher-Level Lampen Objekte
        self.lightingKeys = self.lightController.Lights
        self.stripKey = getStrihallpKey()

        self.connected = True


    def setAmbientLight(self):
        # TEST: Licht an
        for i in self.lightingKeys:
            self.lightController.setLightOn(i)

