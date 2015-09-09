#!/usr/bin/python

from genmap import GenerateGoogleMap
from dp import DouglasPeucker

if __name__ == '__main__':
    mydp = DouglasPeucker()
    delta = 0.00015
    mydp.compress('Data/Uncompressed/cycling_trajectory_20120916.txt', 'Data/Compressed/compressed_cycling_trajectory_20120916.txt', delta)
    
    g = GenerateGoogleMap()
    colors = ['#FF0000', '#FF00FF']
    files = ['Data/Uncompressed/cycling_trajectory_20120916.txt', 'Data/Compressed/compressed_cycling_trajectory_20120916.txt']
    g.gen_googlemap(files, colors, 12, -27.5051212311, 153.028198242, 'Data/cycling_trajectory_20120916.html')