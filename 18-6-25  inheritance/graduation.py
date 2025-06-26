# inheritance sub classes: first, second, third
class graduation:
    def __init__(self):
        pass
    @staticmethod
    def graduate():
        print("congratulations you are a graduate now")

class cse(graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Degree():
        print("congratulations you are a cse student")

class bioinformatics(graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Degree():
        print("congratulations you are a bioinformatics student")

class mtech(graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Degree():
        print("congratulations you are an ece student")

# Example usage:
graduation.graduate()
cse.Degree()
bioinformatics.Degree()
mtech.Degree()