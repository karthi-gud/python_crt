#subclass,super class implementation 
class father:
    def __init__(self):
        pass
    @staticmethod
    def Work():
        print("Father is working")
class son(father):
    def __init__(self):
        super().__init__()
        print("Son is initialized")
    
    @staticmethod
    def Work():
        father.Work()  # Call the parent static method directly
        print("Son is working")
father.Work()  # Call the static method from the parent class
son.Work()  # Call the static method from the subclass