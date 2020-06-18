#!/bin/bash --login


#$ -N git_job             # Name of the job
#$ -cwd                   # Submit in the current working directory
#$ -pe smp.pe 4           # Use a parallel environment with eight cores
                          # This also sets amount of RAM 8 cores = 8gbs RAM

module load apps/intel-17.0/damask/2.0.2

mpirun -n $NSLOTS DAMASK_spectral --geom image.geom --load xcompress.load

