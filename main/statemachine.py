from enum import Enum
import lightHandler
import controller
import remote

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

        # dictionaries mit den states als keys und calllables (Funktionen) als Werte
        self.enterStateFunctions = {
            States.init:            self.onEnterInit,
            States.control:         self.onEnterControl,
            States.ambientLight:    self.onEnterAmbientLight,
            States.signalStandUp:   self.onEnterSignalStandUp,
            States.signalDrink:     self.onEnterSignalDrink,
            States.terminated:      self.onEnterTerminated
        }

        self.exitStateFunctions = {
            States.init:            self.onExitInit,
            States.control:         self.onExitControl,
            States.ambientLight:    self.onExitAmbientLight,
            States.signalStandUp:   self.onExitSignalStandUp,
            States.signalDrink:     self.onExitSignalDrink,
            States.terminated:      self.onExitTerminated
        }

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
        #   *************************************************       signalStandUp
        elif self.current_state == States.signalStandUp:
            self.signalStandUp()
        #   *************************************************       signalDrink
        elif self.current_state == States.signalDrink:
            self.signalDrink()



    #----------------------------- state Funktionen ------------------------------

    def init(self):
        self.lightHandler.initState()

        self.changeState(States.ambientLight)

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
        self.lightHandler.setAmbientLight(ambientValues)
        self.changeState(States.control)

        # Logging
        # print("ambientLight completed!")

    def signalStandUp(self):
        self.lightHandler.setStandUpLight()
        self.changeState(States.control)
        # lightHandler

    def signalDrink(self):
        self.lightHandler.setDrinkingLight()
        self.changeState(States.control)

    def isTerminated(self):
        if self.current_state == States.terminated:
            return True
        return False

    def changeState(self, toState, fromState=-1):
        if remote.getIsOn():
            self.state = States.control

        if fromState == -1:
            fromState = self.current_state

        # Entsprechende onExit Funktion wird aufgerufen
        self.exitStateFunctions[fromState]()

        # Entsprechende onEnter Funktion wird aufgerufen
        self.enterStateFunctions[toState]()

        self.current_state = toState



    def onEnterInit(self):
        pass

    def onExitInit(self):
        pass



    def onEnterControl(self):
        pass

    def onExitControl(self):
        pass



    def onEnterAmbientLight(self):
        pass

    def onExitAmbientLight(self):
        pass



    def onEnterSignalStandUp(self):
        pass

    def onExitSignalStandUp(self):
        pass



    def onEnterSignalDrink(self):
        pass

    def onExitSignalDrink(self):
        pass



    def onEnterTerminated(self):
        pass

    def onExitTerminated(self):
        pass

