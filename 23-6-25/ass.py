# WAPP to simulate the behaviour of a web page or web browsers back button
# when a user visits a new page push it to the stack
# when the user clicks back pop the top page and go back to the previous page

class Browser:
    def __init__(self):
        self.history = []
    
    def visit(self, page):
        self.history.append(page)
        print(f"Visited {page}")
    
    def back(self):
        if len(self.history) > 1:
            self.history.pop()
            print(f"Back to {self.history[-1]}")
        else:
            print("No pages to go back")

# Testing the browser
browser = Browser()
browser.visit('google.com')
browser.visit('linkedin.com') 
browser.visit('github.com')
browser.back()
browser.back()
browser.back()
browser.back()