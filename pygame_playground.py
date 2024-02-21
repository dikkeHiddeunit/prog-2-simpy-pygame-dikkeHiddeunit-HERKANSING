import pygame

pygame.init()

scherm = pygame.display.set_mode((800, 600))
draw = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            draw = True
    scherm.fill((0, 0, 0))

    if draw:
        pygame.draw.rect(scherm, (225, 225, 225), (200, 200, 400, 200))
    pygame.display.flip()