class Remote():
    pass

class Player:
    def moveLeft(self):
        pass
    def moveRight(self):
        pass
    def moveUp(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()