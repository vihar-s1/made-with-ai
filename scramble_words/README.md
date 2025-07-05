# Scramble Words

## Idea

- You will be provided with 7 random letters from the english alphabet.
- Using those letters, you need to form as many words as possible.
- Each word must be a valid English word (validated against a custom list or using some api as well).
- Each new word gains a score equal to its length.
- The game ends when no more words can be formed or you click end.


## Prompt Iteration

### Conversional AI

Grok 3 -- Free Version 

1. 

    Create a scramble words game.

    1. provide user with 7 random letters from english alphabet
    2. User then inputs words formed using those 7 letters.
    3. each letter can be used exactly once.
    4. each valid word  will have a score equal to its length.
    5. word can be validated either by a predefined list or by a api call.
    6. show box titled "Rules" where you explain game rules to user
    7. valid words entered by user should be visible below rules in the order the user entered them.
    8. the game ends when all words are entered or user terminates the game.
    

2. 

    Lets improve the UI.
    1.  Improve the Rules box by centre aligning "Rules" and using numeric bullets
    2. support to submit word by pressing enter key
    3. increase the list size and impove the randomization in letters. The set of letters generated are not always useful.
    4. allow option to shuffle letters (restart game)
    5. show a small alert in red if the word was wrong and in green if the word was right


3. 

    1. Give the UI a more modern look
    2. Improve the valid words listing to more structured an compact format

4.

    1. update the background color, font color for rules since they are both very similar in shade.
    2. update the font color for alert messages as well since they are not visible in the current alert background

5.

    can I instead have an API call integration ??
