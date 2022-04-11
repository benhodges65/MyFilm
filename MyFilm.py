def setUpHouse():
    area1Actions = ["2", "3", "Sit", "Slam Head Against Wall"]
    area1Chances = [40, 30, 10, 20]
    area1 = Area(area1Actions, area1Chances)
    area1Actions = ["1", "8", "4", "Slam Head Against Wall"]
    area1Chances = [40, 30, 10, 20]
    area1 = Area(area1Actions, area1Chances)
class Area:
  def __init__(self, action, chance):
    self.action = action
    self.chance = chance