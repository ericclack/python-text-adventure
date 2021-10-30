# TO DO: add functions to check for directions or actions

def next_player_move(directions, objects):
  "Let the player interact with the room and return their next move"
  
  while True:
    

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

  go = next_player_move()

  
  player_can_take('torch')
  go = which_direction
  
  go = what_to_do(['N', 'S'], ['torch'])


  # All good...
  
  if go == 'N':
    room2()
  if go == 'S':
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
