import lightHandler
import controller
from enum import Enum

# Grundgeruest und zentrale Klasse unserer Zustandsmaschine


class States(Enum):
    init = 0
    control = 1
    ambientLight = 2
    signalStandUp = 3
    signalDrink = 4
    terminated = 5



class Statemachine:
    def __init__(self):
        self.current_state = States.init
        self.lightHandler = lightHandler.LightHandler()
        self.controller = controller.Controller()

    def update(self):
        #   *************************************************       Initialisieren
        if self.current_state == States.init:
            self.init()
        #   *************************************************       Control
        elif self.current_state == States.control:
            self.control()
        #   *************************************************       AmbientLight
        elif self.current_state == States.ambientLight:
            self.ambientLight()



    #----------------------------- state Funktionen ------------------------------

    def init(self):
        self.lightHandler.initState()
        self.current_state = States.ambientLight

        # Logging
        # print("Initialization completed!")

    def control(self):
        signal = self.controller.evaluateSignal()
        if signal == 1:
            self.current_state = States.signalStandUp
        elif signal == 2:
            self.current_state = States.signalDrink
        self.current_state = States.ambientLight

        # Logging
        # print("control completed!")

    def ambientLight(self):
        ambientValues = self.controller.calculateAmbientLight()
        # print(ambientValues)
        # self.lightHandler.setAmbientLight(ambientValues)
        self.current_state = States.control

        # Logging
        # print("ambientLight completed!")

    def isTerminated(self):
        return self.current_state == States.terminated

    def changeToState(self, to):
        pass

