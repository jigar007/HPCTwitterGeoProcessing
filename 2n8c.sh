#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --output=2Cn8c
#SBATCH -t 0-2:00
module load Python/2.7.12-intel-2016.u3 
time srun python geo.py
echo "2 nodes 8 cores"
