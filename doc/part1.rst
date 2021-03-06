.. _part1:

Part 1
======

Trying things out in the console
--------------------------------

On the `Replit`_ website create a new Repl, choosing the Python template, and give it a good title.

You'll see two panels: on the left is your code, and on the right the console, which is where you can try out ideas by typing code to see what happens.

Let's start in the console on the right hand side. Type in the following:

.. code:: python

   print("Welcome to the caves of Xandos")

You should see that text printed on the screen. Pretty easy right?

**Don't be tempted to copy and paste the code from this tutorial!** Typing it in can be slow at first, if you are new to typing, but it will help you understand and remember the code much better than copying will do. 

Now try this:

.. code:: python

   input("What's your name explorer? ")

Great so now we have their name, but how would we modity the welcome message above to welcome them personally?

We need to use a 'variable', which is a place to store things that we might want to use later.

Type these lines in one at a time:

.. code:: python

   player = input("What's your name explorer? ")	  
   print("Welcome to the caves of Xandos,", player)
   
Since we're in the console, we can test out any part of our code, so type these lines one at a time:

.. code:: python

   player

   player.upper()

   player = "Eric"

   player

You can see from the code above that you can change variables. This is handy, later in the tutorial we'll create a variable to store objects found and we'll want to change this as the player plays the game.

Writing the program
-------------------

Let's move over onto the left hand side and put our code into a program file. This means we can run it again later and share it with others.

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

From before you've seen that you can type things in the console, so do that now, type in: :code:`go` to see what's in the variable.

Now imagine all the things that other people could have typed, could be (assuming they chose left):

.. code:: python

   'left'
   'Left'
   'LEFT'
   'letf'
   'l'

That's a lot of possibilities and they all mean left. We want our program to cope with these and do the right thing, so an easy thing to do is take the first letter and lowercase it, then we should always have an 'l' if they want to go left and an 'r' if they want to go right.

Add this line under the `input` statement: 

.. code:: python

   go = go[0].lower()

Did you notice that the first letter is numbered zero? This is the case in most programming languages, counting in lists starts at zero.

So now we can check the `go` variable and send the player to the right place. We'll do this with an if-statement. Add the code to the end of your program:

.. code:: python

   if go == 'l':
      print("You have chosen the left tunnel")
   if go == 'r':
      print("You have chosen the right tunnel")


This works OK but there are some bugs. Try answering the question with something other than 'l' or 'r' and the program just ends. Of if you enter nothing (just press return) and you'll see an error:

.. code:: python

   IndexError: string index out of range

Let's fix these bugs now.

A better way to ask for directions
----------------------------------

We can make a function: this is a way to package up a bit of code so that we can reuse it wherever we linke. 

The function will ask which direction the player wants to go in and perform all the checks we need. This makes sense because we'll be asking the player often and we don't want to repeat ourselves. 

To make a function we use the :code:`def` keyword, like you see below. So add this code to the *start* of your program:

.. code:: python

   def which_direction():
     go = input("Which way do you want to go, left or right? ")
     go = go[0].lower()
     return go

Did you notice that the second, third and fourth lines have two spaces at the start of the line? This means the lines are *indented*, it is how we tell Python that these lines are *inside* the function.

On the last line of the function we use :code:`return` to send back the value to the code that called it. So we can update our program so that it now looks like this, with new code in yellow:

.. code-block:: python
   :emphasize-lines: 1-4,15

   def which_direction():
     go = input("Which way do you want to go, left or right? ")
     go = go[0].lower()
     return go

     
   player = input("What's your name explorer? ")	  
   print("Welcome to the caves of Xandos,", player)

   print()
   print("You are standing in the entrance to a huge cave network.")
   print("You can see a torch on the ground, and can see two tunnels")
   print("one on the left, one on the right")

   go = which_direction()
   if go == 'l':
      print("You have chosen the left tunnel")
   if go == 'r':
      print("You have chosen the right tunnel")

At the moment, this is the same behaviour as before with the same bugs. 

Let's think about the behaviour we want:

- Only accept l and r
- If the user enters something else, ask again

OK, so update your function as follows to fix these bugs:

.. code-block:: python
   :emphasize-lines: 3, 5, 7-10
      
   def which_direction():

     while True:
       go = input("Which way do you want to go, left or right? ")
       if go == "": continue
       go = go[0].lower()
       if go in ['l', 'r']:
	 return go
       else:
	 print("I don't understand")

What do those new lines mean?

- :code:`while True` means keep repeating until we leave with :code:`return`
- :code:`if go == "": continue` means that we try again if the player didn't enter anything
- :code:`if go in ['l', 'r']` checks to see if the user entered an `l` or an `r`.

Test the new code out, you should see that we now have a robust way to ask for a direction from the player.

Adding more rooms
-----------------

Let's add rooms for the left and right tunnels. From now on, every room will be a new function, and they'll all look pretty similar in structure. Add these two functions to the start of your program:

.. code:: python

   def room2():
     print()
     print("You crawl through into a small space, it is quite dark")

   def room3():
     print()
       print("You crawl through the tunnel and stumble, you see")
       print("immediately below you a huge hole and fall to your death!")

So how do we link these up to our existing code?

We change the code after each `if` statement, so where from before you have:

.. code:: python
	  
   if go == 'l':
      print("You have chosen the left tunnel")
   if go == 'r':
      print("You have chosen the right tunnel")

Change it to: 

.. code:: python
	  
   if go == 'l':
      room2()
   if go == 'r':
      room3()

In the next part we'll have a think about the game world and add many more rooms. Read on to :ref:`Part2`.
   
.. _replit: https://replit.com/
