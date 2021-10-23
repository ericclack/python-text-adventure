.. _part3:

Part 3
======

Picking things up
-----------------

Do you remember we said back in :ref:`Part1` that there was a torch in the first room? Let's make it possible for the player to pick this up.

[Coming soon]

.. code:: python

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
