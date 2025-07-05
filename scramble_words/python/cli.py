#!/usr/bin/env python3

from word_scramble import WordScrambleGame

if __name__ == "__main__":
    game = WordScrambleGame()
    game.generate_letters()
    print("Welcome to Word Scramble Game!")
    print("Rules:")
    print("1. You are given 7 random letters (2 vowels, 5 consonants).")
    print("2. Form words using these letters; each letter can be used only once per word.")
    print("3. Each valid word scores points equal to its length.")
    print("4. Commands: 'submit <word>', 'shuffle', 'end', 'restart', 'quit'")
    print("5. Valid words are checked using WordsAPI and displayed with scores.")
    print(game.get_game_state())

    while True:
        command = input("\nEnter command (e.g., 'submit word', 'shuffle', 'end', 'restart', 'quit'): ").strip().lower()
        if command == 'quit':
            print("Thanks for playing!")
            break
        elif command == 'shuffle':
            print(game.shuffle_letters())
        elif command == 'end':
            print(game.end_game())
        elif command == 'restart':
            print(game.restart_game())
        elif command.startswith('submit '):
            word = command[7:].strip()
            print(game.submit_word(word))
        else:
            print("Invalid command! Use 'submit <word>', 'shuffle', 'end', 'restart', or 'quit'.")
        if not game.game_over:
            print(game.get_game_state())
        else:
            print(f"Final Score: {game.total_score}")