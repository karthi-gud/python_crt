class mobile:
    def __init__(self):
        print("object is created")
    
    def unlockmobile(self):
        print("swipe up to unlock your mobile")
    
    def unlockmobile2(self, password):
        print("enter password to unlock your mobile")
    
    def unlockmobile3(self, name, pattern):
        print("enter your pin to unlock your mobile")

m1 = mobile()
m1.unlockmobile()
m1.unlockmobile2("asd123")
m1.unlockmobile3(4, "aasds")

