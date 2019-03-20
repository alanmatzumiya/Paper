Numerical approximation of the Fishers-KPP Stochastic equation.
====================================================
Solves the Fishers-KPP Stochastic equation on 1D using Spectral method based on the spectral decomposition of the Ornstein-Uhlenbeck semigroup associated to the Kolmogorov equation and compute the norm between two solutions with different initial conditions for a fixed point in real space.
----------------------------------------------------------------------------------------------------------

### Simulation Considerations.

Initial Condition (1).

<a href="https://www.codecogs.com/eqnedit.php?latex=u(x)&space;=&space;\frac{1}{\cosh{(5&space;(x&space;-&space;0.5))}^2},&space;\hspace{2mm}&space;x&space;\in&space;[0,&space;1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(x)&space;=&space;\frac{1}{\cosh{(5&space;(x&space;-&space;0.5))}^2},&space;\hspace{2mm}&space;x&space;\in&space;[0,&space;1]" title="u(x) = \frac{1}{\cosh{(5 (x - 0.5))}^2}, \hspace{2mm} x \in [0, 1]" /></a>

Initial Condition (2).

Approximation with Chebyshev Polynomials

<a href="https://www.codecogs.com/eqnedit.php?latex=u(x)&space;\approx&space;\sum^{7}_{n=0}&space;a_n&space;T_n(x),&space;\hspace{2mm}&space;x&space;\in&space;[0,&space;1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(x)&space;\approx&space;\sum^{7}_{n=0}&space;a_n&space;T_n(x),&space;\hspace{2mm}&space;x&space;\in&space;[0,&space;1]" title="u(x) \approx \sum^{7}_{n=0} a_n T_n(x), \hspace{2mm} x \in [0, 1]" /></a>

### Parameters of the simulation for (1) and (2).

<a href="https://www.codecogs.com/eqnedit.php?latex=\nu&space;=&space;0.1,&space;\hspace{2mm}&space;\math{N}&space;=&space;7,&space;\hspace{2mm}&space;\math{M}&space;=&space;20,&space;\hspace{2mm}&space;t&space;\in&space;[0,&space;10]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\nu&space;=&space;0.1,&space;\hspace{2mm}&space;\math{N}&space;=&space;7,&space;\hspace{2mm}&space;\math{M}&space;=&space;20,&space;\hspace{2mm}&space;t&space;\in&space;[0,&space;10]" title="\nu = 0.1, \hspace{2mm} \math{N} = 7, \hspace{2mm} \math{M} = 20, \hspace{2mm} t \in [0, 10]" /></a>

with a discretization of 512 points in space and 256 points in time.

The folder called 'Generated_Data' contains the data produced in the simulation given by the code 'main.py'. For more information about the data read 'README.md' that is contained in this folder.

The folder called 'Graphics' contains the figures produced by the Python codes 'make_graphs.py' and 'Graphics.py'

The Python code 'main.py' returns the discretization of space and time; also returns the numerical approximations for the initial conditions (1) and (2), and the distances between them using the norm established in the paper.
