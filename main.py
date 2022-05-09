class cat :
    def __init__(self, name=None):
        self.name = name
    def __del__(self):
        print("Go eat. The food is already in the bowls.!")
Tom = cat()


class dog:
    def __init__(self, name=None):
        self.name = name
    def __del__(self):
        print("Go eat. The food is already in the bowls.!")
Jack = dog()
