import time

class Player: pass
player = Player()
player.items = []

class Room:
  def __init__(self, directions, items=[]):
    self.directions = directions
    self.items = items
    

def player_action(room):

  while True:
    c = input(f"What do you want to do {player.name}? ")
    try:
      (verb, noun) = c.lower().split(" ")
    except ValueError:
      print("I don't understand")
      continue

    if verb == "go":
      if noun[0] in room.directions: break
      else: print(f"You can't go in direction {noun}")
    elif verb == "take":
      if noun in room.items: break
      else: print(f"There is no {noun} to take")
    else:
      print("I only understand two commands: go, take")
      
  return verb, noun


def sprint(s=""):
  print(s)
  time.sleep(0.2)


def welcome():
  player.name = input("What's your name explorer? ")	  
  print(f"Welcome to the caves of Xandos, {player.name}")

  
entrance_room = Room(['n', 's'], ['torch'])

def entrance():
  sprint()
  sprint("You are standing in the entrance to a huge cave network.")
  if 'torch' in entrance_room.items: 
    sprint("You can see a torch on the ground.")
  sprint("You can see two tunnels, one to the North, one on the South")

  while True: 
    (verb, noun) = player_action(entrance_room)

    if verb == "go":
      if noun[0] == 'n':
        room2()
      if noun[0] == 's':
        room3_death()

    if verb == "take":
      if noun == "torch":
        print("You take the torch")
        player.items.append('torch')
        entrance_room.items.remove('torch')

        
room2_room = Room(['e', 's'])

def room2():
  sprint()
  sprint("You crawl through into a small space")
  if not "torch" in player.items:
    sprint("It is really dark and you can't see much. Maybe you need a torch?")
  else: 
    sprint("You can just make out a hole to the east leading to a")
    sprint("space below, and to the south you can see a tunnel.")

  while True:
    (verb, noun) = player_action(room2_room)

    if verb == "go":
      if noun[0] == 'e':
        room5()
      if noun[0] == 's':
        entrance()

    
def room3_death():
  sprint()
  sprint("You crawl through the tunnel and stumble,")
  sprint("you see immediately below you a huge hole and fall to your death!")

  
room5_room = Room(['n', 'e', 's', 'w'])

def room5():
  sprint("Climing up...")

  while True:
    (verb, noun) = player_action(room5_room)

    if verb == "go":
      if noun[0] == 's':
        room6()


room6_room = Room(['n'], ['key'])

def room6():
  sprint("You're in a small room with only one passage way, the one")
  sprint("you just crawled through.")
  if 'key' in room6_room.items:
    sprint("You see a key in the dirt by your feet.")

  while True:
    (verb, noun) = player_action(room6_room)

    if verb == "go":
      if noun[0] == 'n':
        room5()

    if verb == "take":
      if noun == "key":
        print("You take the key")
        player.items.append('key')
        room6_room.items.remove('key')    

        
welcome()
entrance()
