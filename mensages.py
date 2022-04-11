import pygame.font


class Messages:
    def __init__(self):
        self.font = pygame.font.Font("font/EightBit Atari-Thick.ttf", 34)
        self.font_Atari = "font/EightBit Atari-Thick.ttf"

    def show_text(self, msg, size, color):
        font = pygame.font.Font(self.font_Atari, size)
        message = f'{msg}'
        formatted_text = font.render(message, True, color)
        return formatted_text
      
