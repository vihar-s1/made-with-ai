#!/usr/bin/env python3

import random

class MergeWords:
    def __init__(self):
        self.dictionary = ["the", "cat", "dog", "hat", "rat", "bat", "mat", "sat", "fat", "pat", "tat", "eat", "tea", "ate", "eta"]
        self.tiles = []
        self.selected_tiles = []
        self.score = 0
        self.found_words = []
        self.initialize_game()

    def initialize_game(self):
        self.tiles = self.generate_tiles()
        self.selected_tiles = []
        self.score = 0
        self.found_words = []

    def generate_tiles(self):
        tile_options = [
            ['t', 'h', 'e'], ['c', 'a'], ['t'], ['d', 'o'], ['g'],
            ['h', 'a'], ['t', 'e'], ['c', 'a', 't'], ['d', 'o', 'g']
        ]
        random.shuffle(tile_options)
        return tile_options[:9]

    def select_tile(self, index):
        if 0 <= index < len(self.tiles) and index not in self.selected_tiles:
            self.selected_tiles.append(index)
            return True
        return False

    def backspace(self):
        if self.selected_tiles:
            self.selected_tiles.pop()
            return True
        return False

    def get_current_word(self):
        return ''.join(''.join(self.tiles[i]) for i in self.selected_tiles)

    def submit_word(self):
        word = self.get_current_word()
        if not word:
            return False, "No tiles selected"
        if word in self.found_words:
            self.selected_tiles = []
            return False, "Word already used"
        if word.lower() in self.dictionary:
            self.score += len(word)
            self.found_words.append(word)
            self.selected_tiles = []
            return True, f"Valid word! Score: {self.score}"
        else:
            self.selected_tiles = []
            return False, "Invalid word"

    def shuffle_tiles(self):
        self.tiles = self.generate_tiles()
        self.selected_tiles = []

    def is_game_over(self):
        return len(self.generate_possible_words()) == 0

    def generate_possible_words(self):
        words = []
        for i in range(1, len(self.tiles) + 1):
            for combo in self.get_combinations(list(range(len(self.tiles))), i):
                word = ''.join(''.join(self.tiles[j]) for j in combo)
                if word.lower() in self.dictionary and word not in self.found_words:
                    words.append(word)
        return words

    def get_combinations(self, arr, k):
        results = []
        def combine(curr, start, k):
            if len(curr) == k:
                results.append(curr[:])
                return
            for i in range(start, len(arr)):
                curr.append(arr[i])
                combine(curr, i + 1, k)
                curr.pop()
        combine([], 0, k)
        return results