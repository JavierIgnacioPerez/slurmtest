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
if not os.path.exists("results/test1"):
  os.mkdir("results/test1")

# Simulation sim
ftrain = 0.05
while ftrain <= 1:
  # Creates aux strings.
  amp_s = "amp_" + str(amp) + "_"
  ftrain_s = "ftrain_" + str(ftrain)
  # Creates file with garbage
  np.savetxt("results/test1/" + amp_s + ftrain_s + ".txt", [0, 1])
  # Increments
  ftrain += 0.01
  ftrain = round(ftrain,2)
