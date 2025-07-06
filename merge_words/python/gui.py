#!/usr/bin/env python3

import asyncio
import platform
import pygame
import numpy as np
from merge_words import MergeWords

FPS = 60
TILE_SIZE = (80, 100)
BUTTON_HEIGHT = 50
FONT_SIZE = 24

async def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Merge Words")
    font = pygame.font.SysFont('arial', FONT_SIZE)
    game = MergeWords()
    is_dark_theme = False

    # Sound effects
    def play_sound(frequency, duration=0.1):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * frequency * t) * 0.5
        stereo = np.vstack((wave, wave)).T.astype(np.float32)
        sound = pygame.sndarray.make_sound(stereo)
        sound.play()

    # Colors
    def get_colors():
        return {
            'bg': (237, 242, 247) if not is_dark_theme else (26, 32, 44),
            'tile': (255, 255, 255) if not is_dark_theme else (45, 55, 72),
            'tile_border': (160, 174, 192) if not is_dark_theme else (74, 85, 104),
            'tile_selected': (104, 211, 145) if not is_dark_theme else (56, 161, 105),
            'text': (45, 55, 72) if not is_dark_theme else (226, 232, 240),
            'button': (34, 197, 94) if not is_dark_theme else (52, 211, 153),
            'button_hover': (22, 163, 74) if not is_dark_theme else (44, 181, 130),
            'rules_bg': (226, 232, 240) if not is_dark_theme else (45, 55, 72)
        }

    # Buttons
    buttons = [
        {'text': 'Submit', 'rect': pygame.Rect(10, 350, 80, BUTTON_HEIGHT), 'action': lambda: game.submit_word(), 'sound': 500},
        {'text': 'Shuffle', 'rect': pygame.Rect(110, 350, 80, BUTTON_HEIGHT), 'action': game.shuffle_tiles, 'sound': 400},
        {'text': 'Backspace', 'rect': pygame.Rect(210, 350, 80, BUTTON_HEIGHT), 'action': game.backspace, 'sound': 300},
        {'text': 'Reset', 'rect': pygame.Rect(10, 10, 80, BUTTON_HEIGHT), 'action': game.initialize_game, 'sound': 600},
        {'text': 'Theme', 'rect': pygame.Rect(210, 10, 80, BUTTON_HEIGHT), 'action': lambda: toggle_theme(), 'sound': 350}
    ]

    def toggle_theme():
        nonlocal is_dark_theme
        is_dark_theme = not is_dark_theme

    def draw():
        colors = get_colors()
        screen.fill(colors['bg'])

        # Rules
        rules_rect = pygame.draw.rect(screen, colors['rules_bg'], (10, 60, 280, 100), border_radius=5)
        rules_text = [
            "Merge Words Rules:",
            "1. Click tiles to form a word",
            "2. Submit or Enter to check",
            "3. Score = word length",
            "4. Shuffle, backspace, or reset"
        ]
        for i, line in enumerate(rules_text):
            screen.blit(font.render(line, True, colors['text']), (15, 65 + i * 20))

        # Score and Current Word
        screen.blit(font.render(f"Score: {game.score}", True, colors['text']), (10, 170))
        screen.blit(font.render(f"Word: {game.get_current_word()}", True, colors['text']), (10, 200))

        # Grid
        for i in range(9):
            x, y = (i % 3) * TILE_SIZE[0] + 30, (i // 3) * TILE_SIZE[1] + 230
            color = colors['tile_selected'] if i in game.selected_tiles else colors['tile']
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE[0], TILE_SIZE[1]), border_radius=5)
            pygame.draw.rect(screen, colors['tile_border'], (x, y, TILE_SIZE[0], TILE_SIZE[1]), 2, border_radius=5)
            text = font.render(''.join(game.tiles[i]), True, colors['text'])
            text_rect = text.get_rect(center=(x + TILE_SIZE[0] // 2, y + TILE_SIZE[1] // 2))
            screen.blit(text, text_rect)

        # Buttons
        for button in buttons:
            color = colors['button_hover'] if button['rect'].collidepoint(pygame.mouse.get_pos()) else colors['button']
            pygame.draw.rect(screen, color, button['rect'], border_radius=5)
            text = font.render(button['text'], True, colors['text'])
            text_rect = text.get_rect(center=button['rect'].center)
            screen.blit(text, text_rect)

        # Found Words
        pygame.draw.rect(screen, colors['rules_bg'], (10, 410, 280, 180), border_radius=5)
        screen.blit(font.render("Found Words:", True, colors['text']), (15, 415))
        for i, word in enumerate(game.found_words[:8]):
            screen.blit(font.render(word, True, colors['text']), (15, 435 + i * 20))

        # Game Over
        if game.is_game_over():
            overlay = pygame.Surface((300, 600))
            overlay.fill((0, 0, 0))
            overlay.set_alpha(128)
            screen.blit(overlay, (0, 0))
            pygame.draw.rect(screen, colors['rules_bg'], (50, 200, 200, 200), border_radius=10)
            screen.blit(font.render("Game Over!", True, colors['text']), (100, 250))
            screen.blit(font.render(f"Score: {game.score}", True, colors['text']), (100, 280))
            play_again_rect = pygame.Rect(100, 320, 100, 40)
            color = colors['button_hover'] if play_again_rect.collidepoint(pygame.mouse.get_pos()) else colors['button']
            pygame.draw.rect(screen, color, play_again_rect, border_radius=5)
            screen.blit(font.render("Play Again", True, colors['text']), (110, 330))

        pygame.display.flip()

    def handle_click(pos):
        for button in buttons:
            if button['rect'].collidepoint(pos):
                play_sound(button['sound'])
                button['action']()
                return
        if game.is_game_over():
            if pygame.Rect(100, 320, 100, 40).collidepoint(pos):
                play_sound(600)
                game.initialize_game()
            return
        for i in range(9):
            x, y = (i % 3) * TILE_SIZE[0] + 30, (i // 3) * TILE_SIZE[1] + 230
            if pygame.Rect(x, y, TILE_SIZE[0], TILE_SIZE[1]).collidepoint(pos):
                game.select_tile(i)
                return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game.is_game_over():
                        play_sound(600)
                        game.initialize_game()
                    else:
                        play_sound(500)
                        game.submit_word()
                elif event.key == pygame.K_BACKSPACE:
                    play_sound(300)
                    game.backspace()

        draw()
        await asyncio.sleep(1.0 / FPS)

    pygame.quit()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())