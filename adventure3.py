def what_to_do(directions, pickups=[]):

  while True:
    print("What do you want to do?")
    if pickups: print("  Take ", pickups)
    print("  Go ", directions)
    w = input("> ")
    if w == "": continue

    (verb, noun) = w.split(" ")
    verb = verb.lower()
    
    if verb == "take":
      if noun in pickups:
        print("TODO: take the", noun)
      else:
        print("There isn't a", noun, "to take")
        
    elif verb == "go":
      go = noun[0].upper()
      if go in directions:
        return go
      else:
        print("I don't understand how to go that way")

      
def welcome():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  
def entrance():
  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One to the North, one on the South")

  go = what_to_do(['N', 'S'], ['torch'])

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
