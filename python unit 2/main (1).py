class Player:
    def play(self):
        print("The player is playing cricket")

class Batsman(Player):
    def play(self):
        print("THE BATSMAN IS BATTING")

class Bowler(Player):
    def play(self):
        print("THE BOWLER IS BOWLING")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
