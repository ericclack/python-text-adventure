
def main():
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  print()
  print("You are standing in the entrance to a huge cave network.")
  print("You can see a torch on the ground, and can see two tunnels")
  print("One on the left, one on the right")

  go = which_direction()

  if go == 'L':
    left_tunnel()
  if go == 'R':
    right_tunnel()


def which_direction():

  while True:
    go = input("Which way do you want to go, left or right? ")
    if go == "": continue
    go = go[0].upper()
    if go in ['L', 'R']:
      return go
    else:
      print("I don't understand")

      
def left_tunnel():
  print()
  print("You are in the left tunnel, it is quite dark")
  print("You see a hole on the left leading to a space below, and to the right you can see a way to climb up into another tunnel.")

  go = which_direction()

  if go == 'L':
    left_up_tunnel()
  if go == 'R':
    right_down_tunnel()

    
def right_tunnel():
  print()
  print("You are in the right tunnel, it is a dead end.")

  
def left_up_tunnel():
  print("Climing up, you slip on a rock...")

  
def right_down_tunnel():
  print("It is a lot deeper than it looks...")


main()
