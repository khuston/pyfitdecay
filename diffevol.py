import numpy as np
from scipy.optimize import differential_evolution

def ExpFitDiffEvol(N, x, y):
    """Fit N-exponential decay to a dataseries (x, y) using differential
    evolution as implemented in scipy.optimize.

    Parameters
    ----------
    N : float
        number of summed exponentials to fit

    x : array
        x values

    y : array
        y values

        returns a, b
        len(a) = N
        len(b) = N

        y(x) = \sum_{i=1}^N a_i \exp ( - b_i x )

        Use of differntial evolution inspired by use of another genetic algorithm
        to perform exponential fit of by Weizhong Zou in
            
            Zou, Weizhong. Larson, Ronald G.
            "A mesoscopic simulation method for predicting the rheology of
            semi-dilute wormlike micellar solutions." Journal of Rheology. 58,
            681 (2014).

    """
    x = np.array(x)
    y = np.array(y)

    bounds = [[min(x), max(x)]]*N + [[min(y), max(y)]]*N

    def objective(s):
        taui, fi = np.split(s, 2)
        x_tiled = np.tile(x, (len(taui), 1)).T
        return np.sum((y - np.sum(fi*np.exp(-x_tiled/taui), axis=1))**2.)

    result = differential_evolution(objective, bounds)
    s = result['x']
    taui, fi = np.split(s, 2)
    return fi, 1./taui
