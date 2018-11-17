import json

isOn = False
isPaused = False


def readData():
    global isOn
    global isPaused
    file = open('../webapp/data.json', 'r')
    binData = file.read()
    if not (len(binData) == 2):
        return
    print(binData[0] + binData[1])
    if binData[0] == '1':
        isOn = True
    elif binData[0] == '0':
        isOn = False
    if binData[1] == '1':
        isPaused = True
    elif binData[1] == '0':
        isPaused = False

    """"with open('../webapp/data.json') as f:
        global isOn
        global isPaused
        data = json.load(f)
        print(json.dumps(data))
        if (data["isOn"] == 'false'):
            isOn = False
        elif (data["isOn"] == 'true'):
            isOn = True
        if (data["isPaused"] == 'false'):
            isPaused = False
        elif (data["isPaused"] == 'true'):
            isPaused = True"""


def getIsOn ():
    readData()
    return isOn

def getIsPaused():
    readData()
    return isPaused