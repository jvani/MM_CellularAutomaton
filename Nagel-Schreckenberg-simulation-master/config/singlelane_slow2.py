from simulation.speedLimits import *
from simulation.trafficGenerators import *

maxFps= 40
#size of the window
size = width, heigth = 750, 600
# in miliseconds
updateFrame = 500

# seed for pseudo random generator
seed = None

lanes = 1
# length of the road
length = 325

maxSpeed = 5

t = 50
l = 50

speedLimits = [SpeedLimit(range=((200, 0), (240, 0)), limit=3, ticks=0),
               SpeedLimit(range=((100, 0), (120, 0)), limit=3, ticks=0)]

# traffic generator that is responsible for generating cars each iteration. 
trafficGenerator = SimpleTrafficGenerator() # this generator at each iteration will generate random(0, 2) cars
slowDownProbability, laneChangeProbability = 0.5, 0.0 # slowDownProbability - from NaSch model. laneChangeProbability - from my model
