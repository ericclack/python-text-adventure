# TO DO: add functions to check for directions or actions

def player_action(directions, objects):

  while True:
    c = input("What do you want to do? ")
    try:
      (verb, noun) = c.lower().split(" ")
    except ValueError:
      print("I don't understand")
      continue

    if verb == "go":
      break
    elif verb == "take":
      break
    else:
      print("I only understand two commands: go, take")
      
  return verb, noun


def welcome():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  
def entrance():
  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One to the North, one on the South")

  (verb, noun) = player_action(['n', 's'], ['torch'])

  if verb == "go":
    if noun[0] == 'n':
      room2()
    if noun[0] == 's':
      room3_death()
        
  if verb == "take":
    if noun == "torch":
      print("You take the torch")     

def room2():
  print()
  print("You crawl through into a small space, it is quite dark")
  print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

  go = what_to_do(['e', 's'])

  if go == 'e':
    room5()
  if go == 's':
    entrance()

    
def room3_death():
  print()
  print("You crawl through the tunnel and stumble, you see immediately below you a huge hole and fall to your death!")

  
def room5():
  print("Climing up...")

  go = what_to_do()

  
welcome()
entrance()
