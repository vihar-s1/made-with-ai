package merge_words.java;

import java.util.*;

public class MergeWords {
    private final List<String> dictionary = Arrays.asList("the", "cat", "dog", "hat", "rat", "bat", "mat", "sat", "fat", "pat", "tat", "eat", "tea", "ate", "eta");
    private List<List<String>> tiles;
    private List<Integer> selectedTiles;
    private int score;
    private List<String> foundWords;

    public MergeWords() {
        initializeGame();
    }

    public void initializeGame() {
        tiles = generateTiles();
        selectedTiles = new ArrayList<>();
        score = 0;
        foundWords = new ArrayList<>();
    }

    private List<List<String>> generateTiles() {
        List<List<String>> tileOptions = Arrays.asList(
            Arrays.asList("t", "h", "e"), Arrays.asList("c", "a"), List.of("t"),
            Arrays.asList("d", "o"), List.of("g"), Arrays.asList("h", "a"),
            Arrays.asList("t", "e"), Arrays.asList("c", "a", "t"), Arrays.asList("d", "o", "g")
        );
        Collections.shuffle(tileOptions);
        return new ArrayList<>(tileOptions.subList(0, 9));
    }

    public boolean selectTile(int index) {
        if (index >= 0 && index < tiles.size() && !selectedTiles.contains(index)) {
            selectedTiles.add(index);
            return true;
        }
        return false;
    }

    public boolean backspace() {
        if (!selectedTiles.isEmpty()) {
            selectedTiles.removeLast();
            return true;
        }
        return false;
    }

    public String getCurrentWord() {
        StringBuilder word = new StringBuilder();
        for (int i : selectedTiles) {
            word.append(String.join("", tiles.get(i)));
        }
        return word.toString();
    }

    public String submitWord() {
        String word = getCurrentWord();
        if (word.isEmpty()) {
            return "No tiles selected";
        }
        if (foundWords.contains(word)) {
            selectedTiles.clear();
            return "Word already used";
        }
        if (dictionary.contains(word.toLowerCase())) {
            score += word.length();
            foundWords.add(word);
            selectedTiles.clear();
            return "Valid word! Score: " + score;
        } else {
            selectedTiles.clear();
            return "Invalid word";
        }
    }

    public void shuffleTiles() {
        tiles = generateTiles();
        selectedTiles.clear();
    }

    public boolean isGameOver() {
        return generatePossibleWords().isEmpty();
    }

    private List<String> generatePossibleWords() {
        List<String> words = new ArrayList<>();
        for (int i = 1; i <= tiles.size(); i++) {
            for (List<Integer> combo : getCombinations(new ArrayList<>(), 0, i)) {
                StringBuilder word = new StringBuilder();
                for (int j : combo) {
                    word.append(String.join("", tiles.get(j)));
                }
                String wordStr = word.toString();
                if (dictionary.contains(wordStr.toLowerCase()) && !foundWords.contains(wordStr)) {
                    words.add(wordStr);
                }
            }
        }
        return words;
    }

    private List<List<Integer>> getCombinations(List<Integer> curr, int start, int k) {
        List<List<Integer>> results = new ArrayList<>();
        if (curr.size() == k) {
            results.add(new ArrayList<>(curr));
            return results;
        }
        for (int i = start; i < tiles.size(); i++) {
            curr.add(i);
            results.addAll(getCombinations(curr, i + 1, k));
            curr.removeLast();
        }
        return results;
    }

    public List<List<String>> getTiles() {
        return tiles;
    }

    public List<Integer> getSelectedTiles() {
        return selectedTiles;
    }

    public int getScore() {
        return score;
    }

    public List<String> getFoundWords() {
        return foundWords;
    }
}