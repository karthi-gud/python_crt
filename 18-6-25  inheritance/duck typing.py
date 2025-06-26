class duck():
    def walk(self):
        print("thapak thapak thapak thapak")
class horse():
    def walk(self):
        print("thap thap thap thap")
def myfunction(obj):
    obj.walk()
d=duck()
h=horse()
myfunction(d)
myfunction(h)
