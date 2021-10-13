
def main():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One to the North, one on the South")

  go = which_direction(['N', 'S'])

  if go == 'N':
    room2()
  if go == 'S':
    room3_death()


def which_direction(choices):

  while True:
    c = ", ".join(choices)
    go = input("Which way do you want to go: " + c + "? ")
    if go == "": continue
    go = go[0].upper()
    if go in choices:
      return go
    else:
      print("I don't understand")

      
def room2():
  print()
  print("You crawl through into a small space, it is quite dark")
  print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

  go = which_direction(['E', 'S'])

  if go == 'E':
    room5()
  if go == 'S':
    main()

    
def room3_death():
  print()
  print("You crawl through the tunnel and stumble, you see immediately below you a huge hole and fall to your death!")

  
def room5():
  print("Climing up...")

  go = which_direction()

  

main()
