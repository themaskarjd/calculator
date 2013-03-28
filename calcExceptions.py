#Scott Snow
#Comp 141, Homework 7
#Python Calculator (CalcExceptions.py)

#Calculator Exceptions
#Sets message to unidentified if error is unknown or message is empty
#Sets message to correct error if there is a problem
class CalcExceptions:
    def __init__(self, message=None):
        if message is None or len(message) == 0:
            self.message = "UNIDENTIFIED ERROR."
        else:
            self.message = "Exception: " + message
    def getMessage(self):
        return self.message
