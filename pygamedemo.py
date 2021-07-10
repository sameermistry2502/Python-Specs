import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.dispaly.set_caption('slither')

pygame.dispaly.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
