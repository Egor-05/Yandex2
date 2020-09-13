class Note:
    def __init__(self, name: str):
        self.name = name

    def play(self):
        print(self.name)