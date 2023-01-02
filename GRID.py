import pygame
import tkinter as tk
from tkinter import messagebox

def drawGrid(w, rows, surface):
    sizebt = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizebt
        y = y + sizebt

        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def main():
    global rows, width
    width = 500
    rows = 20
    win = pygame.display.set_mode((width,width))
    #a = snake((255,0,0),(10,10))
    flag = True
    clock = pygame.time.Clock()

    while flag:
       pygame.time.delay(50)
       clock.tick(10)
       redrawWindow(win)

main()