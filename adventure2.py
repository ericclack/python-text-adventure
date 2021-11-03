def which_direction(choices):

  while True:
    c = ", ".join(choices)
    go = input("Which way do you want to go: " + c + "? ")
    if go == "": continue
    go = go[0].lower()
    if go in choices:
      return go
    else:
      print("I don't understand")

      
def welcome():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  
def entrance():
  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One to the North, one on the South")

  go = which_direction(['n', 's'])

  if go == 'n':
    room2()
  if go == 's':
    room3_death()


def room2():
  print()
  print("You crawl through into a small space, it is quite dark")
  print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

  go = which_direction(['e', 's'])

  if go == 'e':
    room5()
  if go == 's':
    entrance()

    
def room3_death():
  print()
  print("You crawl through the tunnel and stumble, you see immediately below you a huge hole and fall to your death!")

  
def room5():
  print("Climing up...")

  go = which_direction()

  
welcome()
entrance()
