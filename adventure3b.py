# TO DO: add functions to check for directions or actions

def player_action(directions, objects):
  "Let the player interact with the room and return their next move"
  
  while True:
    c = input("What do you want to do? ")
    (noun, verb) = c.lower().split(" ")

    if noun == "go":
      if verb[0] in directions:
        break
      else: 
        print("You can't go that way!")

    elif noun == "take":
      if verb in objects:
        break
      else: 
        print("There isn't a", verb, "to take!")

  return noun, verb


def welcome():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  
def entrance():
  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One to the North, one on the South")

  """
  What do you want to do?
  > take torch
  You take the torch, luckily for you it works!
  
  What do you want to do?
  > go north
  You go north...
  """

  (noun, verb) = player_action(['n', 's'], ['torch'])
  
  if noun == "go" and verb[0] == 'n':
    room2()
  if noun == "go" and verb[0] == 's':
    room3_death()


def room2():
  print()
  print("You crawl through into a small space, it is quite dark")
  print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

  go = what_to_do(['E', 'S'])

  if go == 'E':
    room5()
  if go == 'S':
    entrance()

    
def room3_death():
  print()
  print("You crawl through the tunnel and stumble, you see immediately below you a huge hole and fall to your death!")

  
def room5():
  print("Climing up...")

  go = what_to_do()

  
welcome()
entrance()
