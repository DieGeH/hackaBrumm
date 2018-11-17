import json

isOn = True
isPaused = False

def readData():
    with open('../webapp/data.json') as f:
        data = json.load(f.read())
        isOn = data["isOn"]
        isPaused = data["isPaused"]

def getIsOn ():
    readData()
    return isOn

def getIsPaused():
    readData()
    return isPaused