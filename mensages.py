import pygame.font

class Mensages:
    def __init__(self):
        self.font = pygame.font.Font("font/EightBit Atari-Thick.ttf", 34)
        self.font_Atari = "font/EightBit Atari-Thick.ttf"

    def show_text(self, msg, size, color):
        font = pygame.font.Font(self.font_Atari, size)
        mensage = f'{msg}'
        formated_text = font.render(mensage, True, color)
        return formated_text
      
