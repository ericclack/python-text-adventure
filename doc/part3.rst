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
  
Each command will be a *verb* followed by a *noun*. Let's explore in the REPL on the right side of your screen. Add these lines one at a time -- don't enter the lines that start with a hash (#).

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

* If you enter nothing, you get an error: :code:`ValueError: not enough values to unpack (expected 2, got 1)`
* If you enter too many words, e.g. take the apple, you get an error: :code:`ValueError: too many values to unpack (expected 2)`
* You can use any verb, e.g. eat apple
* You can ask to go in any direction, not just those available, e.g. go west
* You can try taking things that don't exist: take apple

Let's fix these one at a time.

In the first two, `ValueError` is Python's way of saying that when we try and split the player's input it won't match a verb and noun. 
