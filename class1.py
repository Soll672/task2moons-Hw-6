class Hello:
    def __init__(self):
        pass

class NewHello(Hello):
    def __init__(self):
        super().__init__()

    def tptint(self):
        print("PYTHON")
