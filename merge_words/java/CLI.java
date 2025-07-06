package merge_words.java;

import java.util.List;
import java.util.Scanner;

public class CLI {
    public static void main(String[] args) {
        MergeWords game = new MergeWords();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Merge Words CLI");
        System.out.println("Rules: Select tiles (0-8) to form words. Enter 's' to shuffle, 'b' to backspace, 'q' to quit.");
        System.out.println("Submit with 'enter'. Score points equal to word length.");

        label:
        while (true) {
            System.out.println("\nScore: " + game.getScore());
            System.out.println("Current Word: " + game.getCurrentWord());
            System.out.println("Found Words: " + (game.getFoundWords().isEmpty() ? "None" : String.join(", ", game.getFoundWords())));
            printGrid(game.getTiles(), game.getSelectedTiles());

            if (game.isGameOver()) {
                System.out.println("Game Over! Final Score: " + game.getScore());
                System.out.print("Play again? (y/n): ");
                String choice = scanner.nextLine().trim().toLowerCase();
                if (!choice.equals("y")) {
                    break;
                }
                game.initializeGame();
                continue;
            }

            System.out.print("Enter tile number (0-8), 's' to shuffle, 'b' to backspace, 'enter' to submit, 'q' to quit: ");
            String action = scanner.nextLine().trim().toLowerCase();

            switch (action) {
                case "q":
                    break label;
                case "s":
                    game.shuffleTiles();
                    break;
                case "b":
                    if (game.backspace()) {
                        System.out.println("Removed last tile selection");
                    } else {
                        System.out.println("No tiles to remove");
                    }
                    break;
                case "enter":
                    System.out.println(game.submitWord());
                    break;
                default:
                    try {
                        int index = Integer.parseInt(action);
                        if (game.selectTile(index)) {
                            System.out.println("Selected tile " + index + ": " + String.join("", game.getTiles().get(index)));
                        } else {
                            System.out.println("Invalid or already selected tile");
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid input");
                    }
                    break;
            }
        }
        scanner.close();
    }

    private static void printGrid(List<List<String>> tiles, List<Integer> selectedTiles) {
        for (int i = 0; i < 9; i += 3) {
            String[] row = new String[3];
            for (int j = i; j < i + 3; j++) {
                String tileStr = String.join("", tiles.get(j));
                row[j - i] = selectedTiles.contains(j) ? "[" + tileStr + "]" : j + ": " + String.format("%-5s", tileStr);
            }
            System.out.println(String.join(" | ", row));
        }
        System.out.println();
    }
}