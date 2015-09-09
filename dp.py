import numpy as np
from math import sqrt

class DouglasPeucker(object):
    
    def __init__(self):
        pass
    
    def compress(self, unfn, wfn, delta):
        Q = np.genfromtxt(unfn, delimiter=',')
        indicies = self._douglas_peucker(Q, 0, len(Q)-1, delta)
        
#         print len(Q), 'data points before compressing'
#         print len(indicies), 'data points after compressing'
#         print 'Compress rate:', 1-float(len(indicies))/len(Q)
        
        with open(wfn, 'w') as f:
            for i in indicies:
                f.write(str(Q[i][0]) + ',' + str(Q[i][1]) + '\n')
    
    def _douglas_peucker(self, Q, s, t, delta):
        """Return the subscripts of the Douglas-Peucker simplified trajectory
        
        Keyword arguments:
        Q -- query trajectory (matrix)
        s -- start position
        t -- end position
        delta -- the threshold
        """
        indecies = []
        
        dmax = -float('inf')
        for i in range(s+1,t):
            d = self._perpendicular_dist(Q, s, t, i)
            if d > dmax:
                dmax = d
                idx = i
        if dmax > delta:
            L1 = self._douglas_peucker(Q, s, idx, delta)
            L2 = self._douglas_peucker(Q, idx, t, delta)
            [indecies.append(x) for x in L1]
            [indecies.append(x) for x in L2]
        else:
            indecies.append(s)
            indecies.append(t)
        
        return indecies
    
    def _perpendicular_dist(self, Q, s, t, i):
        x0, y0, x1, y1, x, y = Q[s][0], Q[s][1], Q[t][0], Q[t][1], Q[i][0], Q[i][1]
        # from http://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html
        return abs((x1-x0)*(y0-y)-(x0-x)*(y1-y0))/sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))
    
if __name__ == "__main__":
    dp = DouglasPeucker()
    delta = 0.00015
    
    Q = np.genfromtxt('Data/Uncompressed/cycling_trajectory_20120916.txt', delimiter=',')
    indicies = dp._douglas_peucker(Q, 0, len(Q)-1, delta)
    print len(Q), 'data points before compressing'
    print len(indicies), 'data points after compressing'
    print 'Compress rate:', 1-float(len(indicies))/len(Q)
    
    dp.compress('Data/Uncompressed/cycling_trajectory_20120916.txt', 'Data/Compressed/compressed_cycling_trajectory_20120916.txt', delta)