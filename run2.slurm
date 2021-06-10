#!/bin/bash
#SBATCH --array=0.1-1.0 : 0.1

python3 test2.py  $SLURM_ARRAY_TASK_ID