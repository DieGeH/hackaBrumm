from main import statemachine


if __name__ == "__main__":
    s = statemachine.Statemachine()

    while not s.isTerminated():
        s.update()

