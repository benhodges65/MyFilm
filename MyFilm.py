import random

def CreateScript():
    area1Actions = ["2", "3", "Lay on Bed", "Slam Head on wall", "Put on Jacket", "Scream", "Pet Dog", "Pet Cat", "Fall", "Jump", "Dialogue"]
    area2Actions = ["4", "5", "6", "7", "Hit head on washer", "Do some laundry", "Dialogue", "Open Cabinets"]
    area3Actions = ["Brush teeth", "Wash Face", "Cut Yourself", "1", "Sit on Toilet"]
    area4Actions = ["2", "Talk", "Pet Cat", "Lay Down", "Look in Mirror", "Talk", "Jump on Bed"]
    area5Actions = ["2", "Observe the void", "Type Some Stuff", "Play a game", "Slam head on Desk", "Talk", "Spin in Chair", "Shred your hand", "Shred Your Hand", "Drink some water"]
    area6Actions = ["2", "Look in mirror", "Wash your hands", "Talk to self in mirror", "Sit on Toilet", "Punch Mirror"]
    area7Actions = ["2", "8", "9", "Slam head into wall"]
    area8Actions = ["9", "2", "Sit on Couch", "Pet Dog", "Watch TV", "YOU ARE VOID", "Read a Book"]
    area9Actions = ["7", "8", "USE THE KNIFE", "TOUCH THE STOVE", "Eat some chips", "Look Outside", "DO IT", "Drink some Water", "Wash your hands"]
    i = 1
    file1 = open("MyScript.txt", "w") 
    currentArea = 1
    while i < 50:
      if currentArea == 1:
        action = random.choice(area1Actions)
      elif currentArea == 2:
        action = random.choice(area2Actions)
      elif currentArea == 3:
        action = random.choice(area3Actions)
      elif currentArea == 4:
        action = random.choice(area4Actions)
      elif currentArea == 5:
        action = random.choice(area5Actions)
      elif currentArea == 6:
        action = random.choice(area6Actions)
      elif currentArea == 7:
        action = random.choice(area7Actions)
      elif currentArea == 8:
        action = random.choice(area8Actions)
      else:
        action = random.choice(area9Actions)
      if action.isnumeric():
        currentArea = int(action)
        file1.write(str(i) + ". Move to room " + action + "\n")
      else:
        file1.write(str(i) + ". " + action + "\n")
      i = i + 1

CreateScript()

