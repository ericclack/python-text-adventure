.. _part3:

Part 3
======

Picking things up
-----------------

Do you remember we said back in :ref:`Part1` that there was a torch in the first room? Let's make it possible for the player to pick this up.

At the moment the player can only state a dirction to go in, by typing N, E, S, or W. So we need to expand the vocabulary that the player can use to make it possible to pick things up, go in directions and for any other actions we think of in the future. 

So instead of just a direction let's ask the player for a command, so that they can enter things like this:

* go west
* take torch
* eat apple

Verbs and nouns
---------------
  
Each command will be a *verb* followed by a *noun*. Let's explore in the console on the right side of your screen. Add these lines one at a time -- don't enter the lines that start with a hash (#).

.. code:: python

   c = input("What do you want to do? ")

   # You'll ender something here like: go east

   c
   c.split(" ")

   # You'll see the first line just returns what you typed, but
   # the second returns a list of [noun, verb], that's just
   # what we need!

   (verb, verb) = c.split(" ")
   if verb == "go": print("Going", noun)

   # Assuming you entered "go ..." then you should see Python
   # spot this.

So hopefully you can see from the examples above that we can ask the player for instructions and understand them.

Let's add a new function so that we can add this to our adventure!

Add this code to the top of your program:

.. code:: python

   def player_action(directions, objects):
     c = input("What do you want to do? ")
     (verb, noun) = c.lower().split(" ")
     return verb, noun

You might notice that we've stopped checking what the player types in. We'll come to that soon, but let's first see how we call this function. 

Now change your entrance function like so:

.. code-block:: python
   :emphasize-lines: 7-17

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

Test it and see if that works. It is quite likely that if you go north or south you'll get an error because we've not changed the rooms to use this new function yet.

Fixing the errors
-----------------

Let's do some testing to see what errors we can find. Have a play and write down everything that doesn't work -- there's quite a list!

When you've done that, scroll down and see if your list matches ours...

...

...

...

...

...

Bug list
........

1. If you enter nothing, you get an error: :code:`ValueError: not enough values to unpack (expected 2, got 1)`
2. If you enter too many words, e.g. take the apple, you get an error: :code:`ValueError: too many values to unpack (expected 2)`
3. You can use any verb, e.g. eat apple
4. You can ask to go in any direction, not just those available, e.g. go west
5. You can try taking things that don't exist: take apple

Let's fix these one at a time.

Not the right number of words
.............................

In the first two errors, `ValueError` is Python's way of saying that when we try and split the player's input it won't match our two variables: verb and noun. 

We can catch this error and ask the player to try again. Let's change your `player_action` function to do this:

.. code-block:: python
   :emphasize-lines: 3,5,7,8,9
      
   def player_action(directions, objects):

     while True:
       c = input("What do you want to do? ")
       try:
	 (verb, noun) = c.lower().split(" ")
	 break
       except ValueError:
	 print("I don't understand")

     return verb, noun

So, what does that all do?

1. You'll have seen :code:`while True` before, it means keep trying until something works and we :code:`break` out of the loop.
2. :code:`try` tells Python that if anything goes wrong, look for a matching :code:`except` for the error.
3. And that's what we see on line 8: :code:`except ValueError`, if this happens we say we don't understand and round we go again.

Only two commands
.................

OK, so the player should only be able to use two commands: `go` in a direction and `take` things. Let's fix this.

Make the following changes to your function:

.. code-block:: python
   :emphasize-lines: 7,10,12-17

   def player_action(directions, objects):

     while True:
       c = input("What do you want to do? ")
       try:
	 (verb, noun) = c.lower().split(" ")
	 # no break here now
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

We've swapped out the :code:`break` and added a :code:`continue`. Continue means go back to the start of the loop, which means the player is asked again for their command.

We'll expand those if-statements in a tick to check for directions and things being taken.

If you haven't tested your new code, go ahead and do this. You should find that errors 1,2 and 3 have been fixed.

Checking the nouns
..................

Finally let's check the directions and objects to squash the last two bugs.

Change your code like so:

.. code-block:: python
   :emphasize-lines: 12,13,15,16

   def player_action(directions, objects):

     while True:
       c = input("What do you want to do? ")
       try:
	 (verb, noun) = c.lower().split(" ")
       except ValueError:
	 print("I don't understand")
	 continue

       if verb == "go":
	 if noun[0] in directions: break
	 else: print("You can't go in direction", noun)
       elif verb == "take":
	 if noun in objects: break
	 else: print("There is no", noun, "to take")
       else:
	 print("I only understand two commands: go, take")

     return verb, noun

Updating our room functions
---------------------------

Great, so now we have a function to discover the next player action, so we can update all of our room functions to use this.

We've already changed the :code:`entrance` function, so we can use this as a guide for the other functions.

Here's what `entrance` looks like now:

.. code-block:: python

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

Ahd if we look at one of our other room functions we'll see something like this:

.. code-block:: python

   def room2():
     print()
     print("You crawl through into a small space, it is quite dark")
     print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

     go = what_to_do(['e', 's'])

     if go == 'e':
       room5()
     if go == 's':
       entrance()

Do you see what lines we need to change? Here's an updated function with the new lines in yellow:

.. code-block:: python
   :emphasize-lines: 6,8,9,11,12

   def room2():
     print()
     print("You crawl through into a small space, it is quite dark")
     print("You can just make out a hole to the east leading to a space below, and to the south you can see a tunnel.")

     (verb, noun) = player_action(['e', 's'], [])

     if verb == "go":
       if noun[0] == 'e':
	 room5()
       if noun[0] == 's':
	 entrance()

Next up
-------

In the next part, coming soon, we'll allow our player to pick things up and use them in our world. 
