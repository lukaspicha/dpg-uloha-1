from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank() 

time_ms = 1000;

while(1):
    if rank != 0:
        for p in range(size):
            time.sleep(p * time_ms)
    else:
        for p in range(size):
            print('Ahoj světe z MPI procesu {} z celkoveho poctu {}'.format(p, size))


