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
    termSigStandUp = 4
    signalDrink = 5
    termSigDrink = 6
    terminated = 7



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
            States.termSigStandUp:  self.onEnterTermSigStandUp,
            States.signalDrink:     self.onEnterSignalDrink,
            States.termSigDrink:    self.onEnterTermSigDrink,
            States.terminated:      self.onEnterTerminated
        }

        self.exitStateFunctions = {
            States.init:            self.onExitInit,
            States.control:         self.onExitControl,
            States.ambientLight:    self.onExitAmbientLight,
            States.signalStandUp:   self.onExitSignalStandUp,
            States.termSigStandUp:  self.onExitTermSigStandUp,
            States.signalDrink:     self.onExitSignalDrink,
            States.termSigDrink:     self.onExitTermSigDrink,
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
        #   *************************************************
        elif self.current_state == States.termSigStandUp:
            self.termSigStandUp()
        #   *************************************************
        elif self.current_state == States.termSigDrink:
            self.termSigDrink()
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
            # self.current_state = States.signalStandUp
            self.changeState(States.signalStandUp)
        elif signal == 2:
            # self.current_state = States.signalDrink
            self.changeState(States.signalDrink)
        else:
            self.changeState(States.ambientLight)



    def ambientLight(self):
        ambientValues = self.controller.calculateAmbientLight()

        self.lightHandler.setAmbientLight(ambientValues)
        self.changeState(States.control)


    def signalStandUp(self):
        self.lightHandler.setStandUpLight()
        self.changeState(States.termSigStandUp)
        # lightHandler

    def termSigStandUp(self):
        if self.controller.terminateStandUp():
            self.changeState(States.control)

    def termSigDrink(self):
        if self.controller.terminateStandUp():
            self.changeState(States.control)

    def signalDrink(self):
        self.lightHandler.setDrinkingLight()
        self.changeState(States.termSigDrink)


    def terminated(self):
        # Lampen aus, scheisse an
        self.lightHandler.terminateAll()


    def isTerminated(self):
        return self.current_state == States.terminated

    def changeState(self, toState, fromState=-1):

        print(remote.getIsOn())


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
        ambientValues = self.controller.calculateAmbientLight()
        self.lightHandler.setAmbientLight(ambientValues)


    def onEnterControl(self):
        pass

    def onExitControl(self):
        pass



    def onEnterAmbientLight(self):
        print("AmbientLight entered")

    def onExitAmbientLight(self):
        pass



    def onEnterSignalStandUp(self):
        pass

    def onExitSignalStandUp(self):
        pass



    def onEnterTermSigStandUp(self):
        self.controller.setThresholdStandUp(10)

    def onExitTermSigStandUp(self):
        ambientValues = controller.calculateAmbientLight()
        self.lightHandler.resetStandUpLight(ambientValues)



    def onEnterSignalDrink(self):
        pass

    def onExitSignalDrink(self):
        pass


    def onEnterTermSigDrink(self):
        self.controller.setThresholdDrink(10)

    def onExitTermSigDrink(self):
        ambientValues = controller.calculateAmbientLight()
        self.lightHandler.resetDrinkLight(ambientValues)




    def onEnterTerminated(self):
        pass

    def onExitTerminated(self):
        pass

