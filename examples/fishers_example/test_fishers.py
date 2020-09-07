from numpy import cosh, linspace
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
    return (1.0 / cosh(5.0 * (x - 0.5)))**2


params = dict(nu=0.1, x=linspace(0, 1, 256), t=linspace(0, 10, 128), N=7)

fisher_solved = FPK_solver(u0, params=params, equation="fisher")
fisher_approx = FPK_solver(fisher_solved.u0_approx, params=params, equation="fisher")

data = fisher_solved.get_data
data_approx = fisher_approx.get_data
distance = fisher_solved.stability(data, data_approx)

fisher_solved.plot.graph_3d()
fisher_approx.plot.graph_3d()
fisher_solved.plot.graph_time([i for i in range(0, 10)], data_approx)
fisher_solved.plot.graph_distance(distance)

# Number of runs
N = 10

# Average time
time = timeit(FPK_solver(u0, params=params, equation="fisher"), number=N) / N

# Save file
file = open('execution_time', 'w')
file.write('execution_time' + ' = ' + str(time) + ' seconds')
file.close()
