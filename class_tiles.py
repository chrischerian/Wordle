class tiles:

    def __init__(self, value, lock):
        self.value = value
        self.lock = lock
    
    def setValue(self, value):
        if self.lock == False:
            self.value = value
            return self.value
        else:
            return self.value
    
    def lockTile(self):
        self.lock = True
    
    def unlockTile(self):
        self.lock = False

    def setColor(self, style):
        style = style
        if style == "green":
            self.value = "\033[42m " + self.value + " \033[0;0m"
            self.lock = True
            return self.value
        elif style == "yellow" and self.lock == False:
            self.value = "\033[103m " + self.value + " \033[0;0m"
            return self.value
        elif style == "black" and self.lock == False:
            self.value = "\033[40m " + self.value + " \033[0;0m"
            self.lock = True
            return self.value
        else:
            return self.value