import time

class Player: pass
player = Player()
player.items = []


def player_action(directions, objects):

  while True:
    c = input(f"What do you want to do {player.name}? ")
    try:
      (verb, noun) = c.lower().split(" ")
    except ValueError:
      print("I don't understand")
      continue

    if verb == "go":
      if noun[0] in directions: break
      else: print(f"You can't go in direction {noun}")
    elif verb == "take":
      if noun in objects: break
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

  
def entrance():
  sprint()
  sprint("You are standing in the entrance to a huge cave network.")
  if 'torch' in entrance.items: 
    sprint("You can see a torch on the ground.")
  sprint("You can see two tunnels, one to the North, one on the South")

  while True: 
    (verb, noun) = player_action(['n', 's'], entrance.items)

    if verb == "go":
      if noun[0] == 'n':
        room2()
      if noun[0] == 's':
        room3_death()

    if verb == "take":
      if noun == "torch":
        print("You take the torch")
        player.items.append('torch')
        entrance.items.remove('torch')

entrance.items = ['torch']


def room2():
  sprint()
  sprint("You crawl through into a small space")
  if not "torch" in player.items:
    sprint("It is really dark and you can't see much. Maybe you need a torch?")
  else: 
    sprint("You can just make out a hole to the east leading to a")
    sprint("space below, and to the south you can see a tunnel.")

  while True:
    (verb, noun) = player_action(['e', 's'], [])

    if verb == "go":
      if noun[0] == 'e':
        room5()
      if noun[0] == 's':
        entrance()

    
def room3_death():
  print()
  print("You crawl through the tunnel and stumble, you see immediately below you a huge hole and fall to your death!")

  
def room5():
  print("Climing up...")

  go = what_to_do()

  
welcome()
entrance()
