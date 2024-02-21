import simpy

def proces(env, naam, actie, duur):
    yield env.timeout(duur)
    print(f'{naam} heeft {actie} om {env.now} uur')

def simpy_playground():
    env = simpy.Environment()
    env.process(proces(env, 'Jaap', 'ontbeten', 8))
    env.process(proces(env, 'Anna', 'gelunched', 13))
    env.process(proces(env, 'Hidde', 'gedineerd', 19))
    env.run()

simpy_playground()