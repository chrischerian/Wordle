from multiprocessing import Lock


class keys:

    def __init__(self, value, color, lock, double, triple):
        self.value = value
        self.color = color
        self.lock = lock
        self.double = double
        self.triple = triple
        
    def lockKey(self):
        self.lock = True

    def setColor(self, style):
        style = style
        if self.lock == True:
            self.color = "\033[32m" + self.value + "\033[0;0m"
            return self.value
        else:
            if style == "green":
                self.color = "\033[32m" + self.value + "\033[0;0m"
                self.lockKey()
                return self.color
            elif style == "yellow":
                self.color = "\033[93m" + self.value + "\033[0;0m"
                return self.color  
            elif style == "black":
                self.color = "\033[30m" + self.value + "\033[0;0m"
                return self.color
            else:
                return self.color

# qKey = keys("Q ", "white", False, False, False)
# print(qKey.setColor("included"))
