from numpy import sin, pi, linspace
from pySpectralFPK import FPK_solver
from timeit import timeit


def u0(x):
    """
    Initial Condition
    Parameters
    ----------
    x : array or float;
        Real space
    Returns
    -------
    array or float : Initial condition evaluated in the real space
    """
    return sin(pi * x)


params = dict(nu=0.01, x=linspace(0, 1, 256), t=linspace(0, 10, 128), N=5)

burgers_solved = FPK_solver(u0, params=params, equation="burgers")
burgers_approx = FPK_solver(burgers_solved.u0_approx, params=params, equation="burgers")

data = burgers_solved.get_data
data_approx = burgers_approx.get_data
distance = burgers_solved.stability(data, data_approx)

burgers_solved.plot.graph_3d()
burgers_approx.plot.graph_3d()
burgers_solved.plot.graph_time([i for i in range(0, 10)], data_approx)
burgers_solved.plot.graph_distance(distance)


# Number of runs
N = 10

# Average time
time = timeit(FPK_solver(u0, params=params, equation="burgers"), number=N) / N

# Save file
file = open('execution_time', 'w')
file.write('execution_time' + ' = ' + str(time) + ' seconds')
file.close()

