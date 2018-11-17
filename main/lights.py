import json
import requests
import colorsys

URL = "http://131.159.211.235"
APIKEY = "/api/99D2ADF803"
Lights = []
StripKey = -1
#Modelid Strip: LIGHTIFY Indoor Flex RGBW
#Modelid Lampe: CLA60 RGBW OSRAM



class Lightse:
    def getLights(self):
        Lights = []
        r = requests.get(URL+APIKEY+"lights/")
        parsed = json.loads(r.json())
        for key in parsed:
            Lights.append(key)
            if parsed[key]["modelid"] == "LIGHTIFY Indoor Flex RGBW":
                StripKey = key
        return

    def ConvertToHSV(self, R, G, B):
        temp = colorsys.rgb_to_hsv(R, G, B)
        h = temp[0]*65535
        s = temp[1]*255
        return s, h

    def setLightColour(self, Key, R, G, B, t=0):
        temp = self.ConvertToHSV(R, G, B)
        d = {"hue": temp[0], "sat": temp[1], "transitiontime": t}
        requests.put(URL+APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightBrightness(self, Key, br, t=0):
        d = {"bri": br, "transitiontime": t}
        requests.put(URL+APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightOff(self, Key, t=0):
        d = {"on": False, "transitiontime": t}
        requests.put(URL+APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def setLightOn(self, Key, t=0):
        d = {"on": True, "transitiontime": t}
        requests.put(URL+APIKEY+"/"+Key+"/state", json.dumps(d))
        return

    def toggleLight(self, Key, t=0):
        r = requests.get(URL+APIKEY+"/lights/"+Key)
        d = json.loads(r.json())
        if not d['state']['on']:
            self.setLightOn(Key, t)
        else:
            self.setLightOff(Key, t)

