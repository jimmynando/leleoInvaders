import pygame


class Player:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.direction = ''

    def move(self, keyPressed):
        if keyPressed[pygame.K_LEFT]:
            self.direction = "LEFT"
        if keyPressed[pygame.K_RIGHT]:
            self.direction = "RIGHT"
        if self.direction == "LEFT":
            if self.x >= 10:
                self.x -= 10
                self.direction = ""
        if self.direction == "RIGHT":
            if self.x <= 320:
                self.x += 10
                self.direction = ""
