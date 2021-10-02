.. _part1:

Part 1
======

Getting Started in the REPL
---------------------------

On the `Replit`_ website create a new Repl, choosing the Python template.

You'll see two panels: on the left is your code, and on the right the REPL, which is where you can try out ideas by typing code to see what happens.

Let's start in the REPL on the right hand side. Type in the following:

.. code:: python

   print("Welcome to the caves of Xandos")

You should see that text printed on the screen. Pretty easy right?

**Don't be tempted to copy and paste the code from this tutorial!** Typing it in can be slow at first, if you are new to typing, but it will help you understand and remember the code much better than copy will do. 

Now try this:

.. code:: python

   input("What's your name explorer? ")

Great so now we have their name, but how would we modity the welcome message above to welcome them personally?

We need to use a 'variable', which is a place to store things that we might want to use later.

Type these lines in one at a time:

.. code:: python

   player = input("What's your name explorer? ")	  
   print("Welcome to the caves of Xandos,", player)
   
Since we're in the REPL, we can test out any part of our code, so type these lines one at a time:

.. code:: python

   player

   player.upper()

   player = "Eric"

   player

You can see from the code above that you can change variables. This is handy, later in the tutorial we'll create a variable to store objects found and we'll want to change this as the player plays the game.

Writing the program
-------------------

Let's move over onto the right hand side and put our code into a program file. This means we can run it again later and share it with others.

.. code:: python

   player = input("What's your name explorer? ")	  
   print("Welcome to the caves of Xandos,", player)

Now you need to click *Run* to see your code in action. 

By the way, do change **any** of the text in quotes -- you might not like caves and it is your adventure!

OK, so what next? Let's describe what they can see. Add the following lines at the end of your program:

.. code:: python

   print()
   print("You are standing in the entrance to a huge cave network.")
   print("You can see a torch on the ground, and can see two tunnels")
   print("one on the left, one on the right")

OK, this is starting to sound like an adventure! So let's ask
the player which way they want to go using `input`:

.. code:: python

   go = input("Which way do you want to go, left or right? ")

Which way to go?
----------------

From before you've seen that you can type things in the REPL, so do that now, type in: :code:`go` to see what's in the variable.

Now imagine all the things that other people could have typed, could be (assuming they chose left):

.. code:: python

   'left'
   'Left'
   'LEFT'
   'letf'
   'l'

That's a lot of possibilities and they all mean left. We want our program to cope with these and do the right thing, so an easy thing to do is take the first letter and uppercase it, then we should always have an 'L' if they want to go left and an 'R' if they want to go right.

Add this line under the `input` statement: 

.. code:: python

   go = go[0].upper()

Did you notice that the first letter is numbered zero? This is the case in most programming languages, counting in lists starts at zero.

Adding more rooms
-----------------

So now we can check the `go` variable and send the player to the right place. We'll do this with an if-statment:


   
.. _replit: https://replit.com/
