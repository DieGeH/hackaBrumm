import json
import requests
import colorsys


#Modelid Strip: LIGHTIFY Indoor Flex RGBW
#Modelid Lampe: CLA60 RGBW OSRAM



class Lightse:

    def __init__(self):
        self.URL = "http://131.159.211.235"
        self.APIKEY = "/api/99D2ADF803"
        self.Lights = []
        self.StripKey = -1

    def getLights(self):
        self.Lights = []
        r = requests.get(self.URL+self.APIKEY+"lights/")
        parsed = json.loads(r.json())
        for key in parsed:
            self.Lights.append(key)
            if parsed[key]["modelid"] == "LIGHTIFY Indoor Flex RGBW":
                self.StripKey = key

        # Logging
        print(self.Lights)
        return

    def ConvertToHSV(self, R, G, B):
        temp = colorsys.rgb_to_hsv(R, G, B)
        h = temp[0]*65535
        s = temp[1]*255
        return s, h

    def setLightColour(self, Key, R, G, B, t=0):
        temp = self.ConvertToHSV(R, G, B)
        d = {"hue": temp[0], "sat": temp[1], "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightBrightness(self, Key, br, t=0):
        d = {"bri": br, "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightOff(self, Key, t=0):
        d = {"on": False, "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightOn(self, Key, t=0):
        d = {"on": True, "transitiontime": t}
        requests.put(self.URL+self.APIKEY+"/"+Key+"/state", json.dumps(d))

        print("self.URL: " + self.URL+self.APIKEY+"/"+Key+"/state")
        print("JSON: " + json.dumps(d))

        return

    def toggleLight(self, Key, t=0):
        r = requests.get(self.URL+self.APIKEY+"/lights/"+Key)
        d = json.loads(r.json())
        if not d['state']['on']:
            self.setLightOn(Key, t)
        else:
            self.setLightOff(Key, t)

