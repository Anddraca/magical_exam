## Things to do for the magical solitaire game

* Make a class for the player's available cards (i.e. hand -- maybe is what I have already?)
* class for the monster stacks
* class for the friendly creatures
* methods for printing the state
* What are things that the player can query for?
  * current monsters
    * current monsters at a given level
  * info for any given card -- need to map ID to name
    * this should likely be priority. Need to modify the original files, NOT make a mapping file
    * that would require updates in two places for changes, violates goals
    * just make the name the ID, adjust from there. It's just a datastore, and the names will be unique (i.e. no two cards with the same name)

* figure out what goes where....
