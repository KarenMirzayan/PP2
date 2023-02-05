class shout:
    def getString(self):
        self.talk = input()
    def printString(self):
        print(self.talk.upper())
p = shout()
p.getString()
p.printString()


        