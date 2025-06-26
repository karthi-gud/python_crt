# multilevel METHOD OVERRIDING
class Grandfather:
    def __init__(self):
        pass
    @staticmethod
    def Property():
        print("100 acres of land")

class Father(Grandfather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Property():
        print("50 acres of land")

class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Property():
        print("25 acres of land")

# Main execution
Grandfather.Property()  # Output: 100 acres of land
Father.Property()       # Output: 50 acres of land
Son.Property()          # Output: 25 acres of land