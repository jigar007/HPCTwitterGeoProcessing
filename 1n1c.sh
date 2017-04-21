#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --output=C1n1c
#SBATCH -t 0-2:00
module load Python/2.7.12-intel-2016.u3
time srun python geo.py
echo "1 nodes 1 core"
