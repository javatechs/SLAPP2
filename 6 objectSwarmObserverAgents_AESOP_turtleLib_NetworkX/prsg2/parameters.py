#parameters.py
from Tools import *

def loadParameters(self):

  # TODO: Update params per PRSG needs
  try: projectVersion = str(common.projectVersion)
  except: projectVersion = "Unknown"
  print "\nProject version "+projectVersion

  mySeed = input("random number seed (1 to get it from the clock) ")
  if mySeed == 1:
        random.seed()
  else:
        random.seed(mySeed)

  self.nAgents = input("How many 'bland' agents? ")

  #self.worldXSize= input("X size of the world? ")
  self.worldXSize=200
  print "X size of the world? ", self.worldXSize

  #self.worldYSize= input("Y size of the world? ")
  self.worldYSize=200
  print "Y size of the world? ", self.worldYSize

  self.nCycles = input("How many cycles? (0 = exit) ")
