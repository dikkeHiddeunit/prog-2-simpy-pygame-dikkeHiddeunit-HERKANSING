'''
Om Simpy en Pygame te combineren, gebruik ik afzonderlijke functies voor Simpy-processimulatie en Pygame-visualisatie.
De Pygame-loop beheert de weergave van het spelvenster en wacht opgebruikersinteractie, 
zoals het indrukken van de spatiebalk om de Simpy-simulatie te starten.
Wanneer ik de spatiebalk indruk, wordt de Simpy-simulatie geactiveerd, waarbij de simulatie van
processen wordt uitgevoerd en relevante informatie wordt afgedrukt in de console. 
Dit zorgt ervoordat Simpy de achterliggende processen van het spel beheert,
terwijl Pygame de visuele weergave beheert.
'''	

import pygame
import simpy

# ------ Simpy ------ 
def proces(env, naam, actie, duur):
    yield env.timeout(duur)
    print(f'{naam} heeft {actie} om {env.now} uur')

def simpy_playground(env):
    env.process(proces(env, 'Jaap', 'ontbeten', 8))
    env.process(proces(env, 'Anna', 'gelunched', 13))
    env.process(proces(env, 'Hidde', 'gedineerd', 19))
    env.run()

'--------------------------------------------------------------------------------------------------------------------------------'

# ------ Pygame -------
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


    if draw:
        env = simpy.Environment()
        simpy_playground(env)
        draw = False

    scherm.fill((0, 0, 0))
    pygame.display.flip()
