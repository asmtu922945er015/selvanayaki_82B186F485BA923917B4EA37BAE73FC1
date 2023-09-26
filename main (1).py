class player:
  def play(self):
    print("the player is playingg cricket.")
class Batsman(player):
  def play(self):
   print("the batman is batting")
class Bowler(player):
  def play(self):
    print("the bowler is boeling.")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()