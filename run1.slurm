#!/bin/bash

#SBATCH -o ./logs/output/%a_%A.out
#SBATCH -e ./logs/error/%a_%A.err
#SBATCH --array=1-10%10

python3 test1.py  $SLURM_ARRAY_TASK_ID
