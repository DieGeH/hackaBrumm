import json
import requests
import colorsys


#Modelid Strip: LIGHTIFY Indoor Flex RGBW
#Modelid Lampe: CLA60 RGBW OSRAM



class Lightse:

    def __init__(self):
        self.URL = "http://131.159.204.65"
        self.APIKEY = "/api/C62742EA77"
        self.Lights = []
        self.StripKey = -1

    def getLights(self):
        # Logging
        print(self.URL+self.APIKEY+"/lights/")

        self.Lights = []
        r = requests.get(self.URL+self.APIKEY+"/lights/")
        parsed = json.loads(r.text)
        print(parsed)
        for key in parsed:
            self.Lights.append(key)
            if parsed[key]["modelid"] == "LIGHTIFY Indoor Flex RGBW":
                self.StripKey = key

        # Logging
        #print(self.Lights)


    def convertToHSV(self, R, G, B):
        temp = colorsys.rgb_to_hsv(R/255.0, G/255.0, B/255.0)
        h = temp[0]*65535
        s = temp[1]*255
        return h, s

    def setLightColour(self, Key, R, G, B, t=0):
        temp = self.convertToHSV(R, G, B)
        d = {"hue": temp[0], "sat": temp[1], "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/lights/"+Key+"/state", json.dumps(d))
        return

    def setLightBrightness(self, Key, br, t=0):
        d = {"bri": br, "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/lights/"+Key+"/state", json.dumps(d))
        return

    def setLightOff(self, Key, t=0):
        d = {"on": False, "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/lights/"+Key+"/state", json.dumps(d))
        return

    def setLightOn(self, Key, t=0):
        print("URL: " + self.URL+self.APIKEY+"/lights/"+Key+"/state")

        #d = {"on": True, "transitiontime": t}
        d = {"on": True}
        r = requests.put(self.URL+self.APIKEY+"/lights/"+Key+"/state", json.dumps(d))

        return

    def toggleLight(self, Key, t=0):
        r = requests.get(self.URL+self.APIKEY+"/lights/"+Key)
        d = json.loads(r.text)
        if not d['state']['on']:
            self.setLightOn(Key, t)
        else:
            self.setLightOff(Key, t)



    def getStripKey(self):
        return self.StripKey


    def getLightKeys(self):
        return self.Lights

