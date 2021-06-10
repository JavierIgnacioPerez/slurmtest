# Gets a value from args for amplitude 
# Amplitude is between 0.1 and 1. Need to be multiple of 0.1
# This need validation.

# This script runs a simulation iterating all the possible values
# for ftrain (0.05kHz to 1 kHz) with a specific value for amplitude

# Writes a file with the results in ./results/test1/...

# Imports
import sys
import os
import numpy as np

# Get data args from bash
amp = sys.argv[0]

# Creates output folder
if not os.path.exists("results"):
  os.mkdir("results")
if not os.path.exists("results/test2"):
  os.mkdir("results/test2")

# Simulation sim
ftrain = 0.05
dist= 100
while ftrain <= 1:
  while dist <= 1000:
    # Creates aux strings.
    amp_s = "amp_" + str(amp) + "_"
    ftrain_s = "ftrain_" + str(ftrain) + "_"
    dist_s = "dist_" + str(dist)
    # Creates file with garbage
    np.savetxt("results/test2/" + amp_s + ftrain_s + dist_s + ".txt", [0, 1])
    # Increments dist
    dist += 100
  # Increments and round ftrain
  dist = 100
  ftrain += 0.01
  ftrain = round(ftrain,2)
