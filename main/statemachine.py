from enum import Enum
import lightHandler.LightHandler

# Grundgeruest und zentrale Klasse unserer Zustandsmaschine


class States(Enum):
    init = 0
    control = 1
    ambientLight = 2
    signalStand = 3
    terminated = 4


class Statemachine:
    def __init__(self):
        self.current_state = States.init
        self.lightHandler = LightHandler()

    def update(self):
        #   *************************************************       Initialisieren
        if self.current_state == States.init:
            self.init()

        #   *************************************************       AmbientLight
        elif self.current_state == States.ambientLight:
            selfambientLight()



    #----------------------------- state Funktionen ------------------------------

    def init(self):
        self.lightHandler.initState()
        self.current_state = States.ambientLight


    def ambientLight(self):
        self.lightHandler.setAmbientLight()


    def isTerminated(self):
        return self.current_state == States.terminated

