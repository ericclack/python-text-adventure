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
  print("You are in the left tunnel, it is quite dark")
  print("You see a hole on the left leading to a space below, and to the right you can see a way to climb up into another tunnel.")

    
def room3():
  print()
  print("You are in the right tunnel, it is a dead end.")

  

player = input("What's your name explorer? ")	  
print("Welcome to the caves of Xandos,", player)

print()
print("You are standing in the entrance to a huge cave network.")
print("You can see a torch on the ground, and can see two tunnels")
print("One heading East, one heading West.")

go = which_direction(['E', 'W'])

if go == 'E':
  room2()
if go == 'W':
  room3()
