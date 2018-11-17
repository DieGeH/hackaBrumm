import json

isOn = False
isPaused = False

def readData():
    with open('data.json') as f:
        data = json.load(f)
        if (data["isOn"] == 'false'):
            isOn = False
        else:
            isOn = True
        if (data["isPaused"] == 'false'):
            isPaused = False
        else:
            isPaused = True

def getIsOn ():
    readData()
    return isOn

def getIsPaused():
    readData()
    return isPaused