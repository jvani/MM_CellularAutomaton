import sys, pygame, simulation.road, simulation.speedLimits, random, importlib, config, csv, os
from simulation.car import Car
from representation import Representation
from simulationManager import SimulationManager
from simulation.trafficGenerators import *
from infoDisplayer import *

if len(sys.argv) != 2:
    print("Usage: python pyTraffic.py module_with_config")
    exit()

config = importlib.import_module(sys.argv[1])

random.seed(config.seed)
pygame.init()
screen = pygame.display.set_mode(config.size)

clock = pygame.time.Clock()

simulation.car.Car.slowDownProbability = config.slowDownProbability
simulation.car.Car.laneChangeProbability = config.laneChangeProbability
speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed)
road = simulation.road.Road(config.lanes, config.length, speedLimits)
simulation = SimulationManager(road, config.trafficGenerator, config.updateFrame)
representation = Representation(screen, road, simulation)
update_count = ''

occ_total = 0
deadcars_tot = 0


while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    simulation.update(dt)

    if len(representation.infoDisplayer.text) > 1:
        if update_count != representation.infoDisplayer.text[2]:
            update_count = representation.infoDisplayer.text[2]
            
            occ_total += float(representation.infoDisplayer.text[5].lstrip('occupancy %:'))
            
            if float(update_count.lstrip('updates: ')) % 300 == 0:
                row = representation.infoDisplayer.text
                
                deadcars = float(row[3].lstrip('dead cars: ')) - deadcars_tot
                deadcars_tot = float(row[3].lstrip('dead cars: '))
                avg_occ = occ_total/300
            
                with open('output.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([deadcars, avg_occ])
                
                occ_total = 0

    representation.draw(dt * simulation.timeFactor)
    pygame.display.flip()


print("Goodbye")
