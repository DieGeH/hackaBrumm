import json

isOn = True
isPaused = False

def readData():
    with open('../webapp/data.json') as f:
        data = json.load(f.read())
        if (data["isOn"] == 'false'):
            isOn = False
        elif (data["isOn"] == 'true'):
            isOn = True
        if (data["isPaused"] == 'false'):
            isPaused = False
        elif (data["isPaused"] == 'true'):
            isPaused = True

def getIsOn ():
    readData()
    return isOn

def getIsPaused():
    readData()
    return isPaused