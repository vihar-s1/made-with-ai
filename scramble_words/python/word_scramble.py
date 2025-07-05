#!/usr/bin/env python3

import random
import requests

class WordScrambleGame:
    API_KEY = 'YOUR_RAPIDAPI_KEY'  # Replace with your RapidAPI key

    def __init__(self):
        self.letters = []
        self.valid_words = []
        self.total_score = 0
        self.game_over = False

    def generate_letters(self):
        """Generate 7 random letters (2 vowels, 5 consonants)."""
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        self.letters = []
        # Add 2 vowels
        for _ in range(2):
            self.letters.append(random.choice(vowels))
        # Add 5 consonants
        for _ in range(5):
            self.letters.append(random.choice(consonants))
        # Shuffle letters
        random.shuffle(self.letters)

    def is_valid_word(self, word):
        """Validate word using WordsAPI and letter constraints."""
        if not word or word in self.valid_words:
            return False, "Word already used or empty!"

        # Check if word can be formed with given letters
        letter_count = {letter: self.letters.count(letter) for letter in self.letters}
        for char in word.lower():
            if char not in letter_count or letter_count[char] == 0:
                return False, "Word uses invalid or too many letters!"
            letter_count[char] -= 1

        # Validate with WordsAPI
        try:
            response = requests.get(
                f"https://wordsapiv1.p.rapidapi.com/words/{word.lower()}",
                headers={
                    'X-RapidAPI-Key': self.API_KEY,
                    'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com'
                }
            )
            if response.status_code == 200:
                return True, "Valid word!"
            else:
                return False, "Not a valid English word!"
        except requests.RequestException as e:
            return False, f"API error: {str(e)}"

    def submit_word(self, word):
        """Submit a word and update game state."""
        if self.game_over:
            return "Game over! Start a new game."
        is_valid, message = self.is_valid_word(word)
        if is_valid:
            self.valid_words.append(word.lower())
            self.total_score += len(word)
        return message

    def shuffle_letters(self):
        """Generate a new set of letters without resetting score."""
        if self.game_over:
            return "Game over! Start a new game."
        self.generate_letters()
        return "Letters shuffled!"

    def end_game(self):
        """End the game and display final score."""
        self.game_over = True
        return f"Game Over! Final Score: {self.total_score}"

    def restart_game(self):
        """Restart the game with new letters and reset state."""
        self.letters = []
        self.valid_words = []
        self.total_score = 0
        self.game_over = False
        self.generate_letters()
        return "Game restarted!"

    def get_game_state(self):
        """Return current game state as a formatted string."""
        return (f"Letters: {' '.join(self.letters)}\n"
                f"Valid Words: {', '.join([f'{w} ({len(w)})' for w in self.valid_words]) or 'None'}\n"
                f"Total Score: {self.total_score}")
