
def main():
    
  player = input("What's your name explorer? ")	  
  print("Welcome to the caves of Xandos,", player)

  while True:
      
    print()
    print("You are standing in the entrance to a huge cave network.")
    print("You can see a torch on the ground, and can see two tunnels")
    print("One on the left, one on the right")

    go = input("Which way do you want to go, left or right? ")
    go = go[0].upper()

    if go == 'L':
      left_tunnel()
    if go == 'R':
      right_tunnel()

    
def left_tunnel():
  print()
  print("You are in the left tunnel, it is quite dark")
  print("You see a hole leading to a space below, and above you can see a way to climb up into another tunnel.")

  go = input("Which way do you want to go, up or down, or back the way you came? ")
  go = go[0].upper()

  if go == 'U':
    up_tunnel()
  if go == 'D':
    down_tunnel()

    
def right_tunnel():
  print()
  print("You are in the right tunnel, it is a dead end.")

  
def up_tunnel():
  print("Climing up, you slip on a rock...")

  
def down_tunnel():
  print("It is a lot deeper than it looks...")


main()
