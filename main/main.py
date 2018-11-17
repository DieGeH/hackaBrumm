import statemachine
import remote
import time


if __name__ == "__main__":
    s = statemachine.Statemachine()
    #main.run(s)

    while not s.isTerminated():
        s.update()
        while not remote.getIsOn():
            print("penuz")
            time.sleep(0.1)

'''
def run(s):
    while remote.getIsOn():
        s.update()
    waitForRun(s)

def waitForRun(s):
    while not remote.getIsOn():
        pass
    run(s)
'''
