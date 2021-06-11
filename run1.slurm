#!/bin/bash
#SBATCH --output=/home/jperezc/tests/SlurmTest/logs/output/%a_%A.txt
#SBATCH --error=/home/jperezc/tests/SlurmTest/logs/error/%a_%A.err
#SBATCH --array=1-10%10

python3 test1.py  $SLURM_ARRAY_TASK_ID