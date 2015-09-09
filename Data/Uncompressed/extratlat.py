#!/usr/bin/python

import numpy as np

traj = np.genfromtxt('cycling_trajectory_20120916_elevation.txt', delimiter=',')
with open('cycling_trajectory_20120916.txt', 'w') as f:
    [f.write(str(L[1])+','+str(L[0])+'\n') for L in traj]