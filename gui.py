# Leave to James — responsive pygame + pygame_gui template
import sys
import pygame
import pygame_gui


pygame.init()
clock = pygame.time.Clock()
# Get display information
displayInfo = pygame.display.Info()
# Chooses starting size (80% of screen size or minimum 640x480 - whichever is larger)
windowWidth = max(int(displayInfo.current_w * 0.8), 640) 
windowHeight = max(int(displayInfo.current_h * 0.8), 480)
# Store window size as a tuple
windowSize = (windowWidth, windowHeight)

print(f"Window size: {windowSize[0]}x{windowSize[1]}")