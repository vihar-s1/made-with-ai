#!/usr/bin/env python3

from merge_words import MergeWords

def print_grid(tiles, selected_tiles):
    for i in range(0, 9, 3):
        row = []
        for j in range(i, i + 3):
            tile_str = ''.join(tiles[j])
            if j in selected_tiles:
                tile_str = f"[{tile_str}]"
            row.append(f"{j}: {tile_str:^5}")
        print(" | ".join(row))
    print()

def main():
    game = MergeWords()
    print("Merge Words CLI")
    print("Rules: Select tiles (0-8) to form words. Enter 's' to shuffle, 'b' to backspace, 'q' to quit.")
    print("Submit with 'enter'. Score points equal to word length.")

    while True:
        print("\nScore:", game.score)
        print("Current Word:", game.get_current_word())
        print("Found Words:", ", ".join(game.found_words) if game.found_words else "None")
        print_grid(game.tiles, game.selected_tiles)

        if game.is_game_over():
            print(f"Game Over! Final Score: {game.score}")
            choice = input("Play again? (y/n): ").lower()
            if choice != 'y':
                break
            game.initialize_game()
            continue

        action = input("Enter tile number (0-8), 's' to shuffle, 'b' to backspace, 'enter' to submit, 'q' to quit: ").lower()
        
        if action == 'q':
            break
        elif action == 's':
            game.shuffle_tiles()
        elif action == 'b':
            if game.backspace():
                print("Removed last tile selection")
            else:
                print("No tiles to remove")
        elif action == 'enter':
            success, message = game.submit_word()
            print(message)
        else:
            try:
                index = int(action)
                if game.select_tile(index):
                    print(f"Selected tile {index}: {''.join(game.tiles[index])}")
                else:
                    print("Invalid or already selected tile")
            except ValueError:
                print("Invalid input")

if __name__ == "__main__":
    main()