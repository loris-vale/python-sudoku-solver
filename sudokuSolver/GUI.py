# GUI.py
import pygame
from solver import solve_grid, valid_grid
import time
pygame.font.init()


class Grid:
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 7, 2, 0, 0, 0],
        [0, 0, 0, 1, 5, 9, 0, 0, 0],
        [0, 0, 0, 8, 3, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows - rows
        self.cols = cols

