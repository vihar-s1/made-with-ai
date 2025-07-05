#!/usr/bin/env python3

import tkinter as tk
from scramble_words.python.cli import WordScrambleGame  # Import the game logic from CLI version


class WordScrambleGUI:
    def __init__(self, root):
        self.game = WordScrambleGame()
        self.root = root
        self.root.title("Word Scramble Game")
        self.root.configure(bg='#111827')  # Dark background (gray-900)
        self.root.geometry("600x700")

        # Main frame
        self.main_frame = tk.Frame(self.root, bg='#1f2937', padx=20, pady=20)  # gray-800
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        tk.Label(self.main_frame, text="Word Scramble Game", font=("Arial", 24, "bold"), bg='#1f2937', fg='white').pack(pady=10)

        # Rules
        rules_frame = tk.Frame(self.main_frame, bg='#eff6ff')  # blue-50
        rules_frame.pack(fill=tk.X, pady=10)
        tk.Label(rules_frame, text="Rules", font=("Arial", 18, "bold"), bg='#eff6ff', fg='#1f2937').pack()
        rules_text = (
            "1. You are given 7 random letters.\n"
            "2. Form words using these letters; each letter can be used once.\n"
            "3. Each valid word scores points equal to its length.\n"
            "4. Submit words via the input box or Enter key.\n"
            "5. End the game with 'End Game'.\n"
            "6. Valid words are shown below.\n"
            "7. Click 'Shuffle Letters' for new letters."
        )
        tk.Label(rules_frame, text=rules_text, font=("Arial", 10), bg='#eff6ff', fg='#1f2937', justify=tk.LEFT).pack(padx=10, pady=5)

        # Letters display
        self.letters_label = tk.Label(self.main_frame, text="", font=("Courier", 16), bg='#374151', fg='white', pady=5)
        self.letters_label.pack(fill=tk.X, pady=10)

        # Input and Submit
        input_frame = tk.Frame(self.main_frame, bg='#1f2937')
        input_frame.pack(fill=tk.X, pady=5)
        self.word_entry = tk.Entry(input_frame, font=("Arial", 12), bg='#374151', fg='white', insertbackground='white')
        self.word_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.word_entry.bind('<Return>', lambda event: self.submit_word())
        tk.Button(input_frame, text="Submit", font=("Arial", 12), bg='#3b82f6', fg='white', activebackground='#2563eb', command=self.submit_word).pack(side=tk.LEFT, padx=5)

        # Shuffle and End buttons
        button_frame = tk.Frame(self.main_frame, bg='#1f2937')
        button_frame.pack(fill=tk.X, pady=5)
        tk.Button(button_frame, text="Shuffle Letters", font=("Arial", 12), bg='#eab308', fg='white', activebackground='#ca8a04', command=self.shuffle_letters).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(button_frame, text="End Game", font=("Arial", 12), bg='#ef4444', fg='white', activebackground='#dc2626', command=self.end_game).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Alert message
        self.alert_label = tk.Label(self.main_frame, text="", font=("Arial", 10), bg='#1f2937', fg='#1f2937')
        self.alert_label.pack(fill=tk.X, pady=5)

        # Valid words and score
        tk.Label(self.main_frame, text="Valid Words:", font=("Arial", 14, "bold"), bg='#1f2937', fg='white').pack()
        self.words_frame = tk.Frame(self.main_frame, bg='#1f2937')
        self.words_frame.pack(fill=tk.BOTH, pady=5)
        self.score_label = tk.Label(self.main_frame, text="Total Score: 0", font=("Arial", 12), bg='#1f2937', fg='white')
        self.score_label.pack(pady=5)

        # Game over frame
        self.game_over_frame = tk.Frame(self.main_frame, bg='#1f2937')
        tk.Label(self.game_over_frame, text="Game Over!", font=("Arial", 16, "bold"), bg='#1f2937', fg='#dc2626').pack()
        self.final_score_label = tk.Label(self.game_over_frame, text="Final Score: 0", font=("Arial", 12), bg='#1f2937', fg='white')
        self.final_score_label.pack()
        tk.Button(self.game_over_frame, text="Restart Game", font=("Arial", 12), bg='#22c55e', fg='white', activebackground='#16a34a', command=self.restart_game).pack(pady=5)

        # Initialize game
        self.update_ui()

    def update_ui(self):
        """Update the GUI with current game state."""
        state = self.game.get_game_state()
        self.letters_label.config(text=state['letters'])
        self.score_label.config(text=f"Total Score: {state['total_score']}")
        self.final_score_label.config(text=f"Final Score: {state['total_score']}")
        
        # Clear and update valid words
        for widget in self.words_frame.winfo_children():
            widget.destroy()
        for i, (word, score) in enumerate(state['valid_words']):
            tk.Label(self.words_frame, text=f"{word} ({score})", font=("Arial", 10), bg='#374151', fg='white').grid(row=i // 2, column=i % 2, padx=5, pady=2, sticky='w')
        
        # Show/hide game over frame
        if state['game_over']:
            self.game_over_frame.pack(fill=tk.X)
            self.word_entry.config(state='disabled')
        else:
            self.game_over_frame.pack_forget()
            self.word_entry.config(state='normal')
        self.word_entry.focus()

    def show_alert(self, message, is_success):
        """Show temporary alert message."""
        self.alert_label.config(text=message, bg='#bbf7d0' if is_success else '#fecaca')
        self.root.after(2000, lambda: self.alert_label.config(text="", bg='#1f2937'))

    def submit_word(self):
        """Handle word submission."""
        if self.game.game_over:
            self.show_alert("Game over! Start a new game.", False)
            return
        word = self.word_entry.get().strip()
        message = self.game.submit_word(word)
        self.show_alert(message, "Valid word!" in message)
        self.update_ui()

    def shuffle_letters(self):
        """Handle shuffle letters."""
        message = self.game.shuffle_letters()
        self.show_alert(message, "shuffled" in message.lower())
        self.update_ui()

    def end_game(self):
        """Handle end game."""
        message = self.game.end_game()
        self.show_alert(message, False)
        self.update_ui()

    def restart_game(self):
        """Handle restart game."""
        message = self.game.restart_game()
        self.show_alert(message, True)
        self.update_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordScrambleGUI(root)
    root.mainloop()