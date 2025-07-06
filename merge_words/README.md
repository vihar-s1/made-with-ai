# Merge Words

## Idea

- A 3x3 grid of tiles is provided. Each tile has a either one/two/three letters on it.
- The player can select tiles in a sequence to form a word.
- On submission, the word is checked against a dictionary.
- A correct word scores points equal to the number of letters in the word.
- The game continues until the player can no longer form any words.
- The player can also choose to shuffle the tiles to get a new arrangement.
- The list of successfult submissions is displayed at the bottom of the screen.
- The player can also choose to reset the game to start over.
- The rules are displayed at the top of the screen in a rule-box.


## Prompt Iteration

### Conversional AI

Grok 3 -- Free Version 

### HTML Prompt Iteration

1. 

    Let's create a new game named "Merge Words"

    1. A 3x3 grid of tiles is provided. Each tile has either one/two/three letters on it.
    2. The player can select tiles in a sequence to form a word.
    3. On submission, the word is checked against a dictionary.
    4. A correct word scores points equal to the number of letters in the word.
    5. The game continues until the player can no longer form any words.
    6. The player can also choose to shuffle the tiles to get a new arrangement.
    7. The list of successful submissions is displayed at the bottom of the screen.
    8. The player can also choose to reset the game to start over.
    9. The rules are displayed at the top of the screen in a rule box.

2. 

    1. Improve the game UI to a more modern, smooth look.
    2. The tiles in the grid should not shuffle every time a word is submitted.
    3. Unique submitted words should be there.
    4. Show the Game ended page when all possible words are covered.
    5. Create a toggle on top to change themes.
    6. Move the Reset Game button to the top.

3.

    1. Improve the grid layout and remove spacing between tiles.  Give the tiles a slightly rectangular shape.
    2. Improve the "Submit Word" and "Shuffle Tiles" button UI.
    3. Improve the dark theme, light theme and iron out some bugs.
    4. Add sound effects for each button click, but not grid tiles.
    5. Create a backspace button to clear the last tile selection.
    6. The Enter button submits, and the backspace button clears

### Python Prompt Iteration

1.

    Now lets generate the same version of the game in python.

    1. I want a 3 files structure for the game.
    2. merge_words.py will contain a class to handle the game logistics.
    3. cli.py should use the game class to implement a CLI version of the game.
    4. gui.py should use the game class to implement a GUI version of the game.


### Java Prompt Iteration

1.

    Now let's generate the same version of the game in java.

    1. I want a 3-file structure for the game.
    2. merge_words.java will contain a class to handle the game logistics.
    3. cli.java should use the game class to implement a CLI version of the game.
    4. gui.java should use the game class to implement a GUI version of the game.