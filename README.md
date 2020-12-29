Numerical approximation of the stochastic Burgers equation and stochastic Fisher–KPP equation.
==============================================================================================

Within each folder there are Python codes, these codes numerically solve the Kolmogorov equation associated with the equation of interest.


pySpectralFPK: Solver for Burgers' Equation (building)
------------

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

`pySpectralFPK` is a Python package for solving Stochastic Partial Differential Equations (SPDEs)
using spectral methods, also contains plot tools to built 3D or 2D graphics about solutions.

Two examples are showed for Burgers' and Fisher's equation in it's stochastic versions. The associated differential operators
are computed using a numba-compiled implementation of spectral methods. This allows defining, inspecting, and solving typical PDEs
that appear for instance in the study of dynamical systems in physics. The focus of the package lies on easy usage to explore the
behavior of SPDEs. However, core computations can be compiled transparently using numba for speed.

[Try it out online!](https://mybinder.org/v2/gh/github.com/alanmatzumiya/Paper/master?filepath=examples%2Fjupyter)

Installation
------------

`pySpectralFPK` is available on `pypi`, so you should be able to install it through
`pip`:

```bash
pip install pySpectralFPK
```

Usage
-----

A simple example showing the evolution of the deterministic equation in 1d:

```python
from numpy import sin, pi, linspace
from pySpectralFPK import FPK_solver


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

# setting parameters
params = dict(nu=0.01, x=linspace(0, 1, 256), t=linspace(0, 10, 128), N=5)

# solve the pde
result = FPK_solver(u0=u0, params=params, equation="burgers")

# plot and save
result.plot.graph_3d(name="test")
```
which can be solved for different values of `Diffusion coefficient` in the example above.


More information
----------------
* The [paper published in the Journal](http://dx.doi.org/10.13140/RG.2.2.21593.47203)

<embed type="application/pdf" href="https://github.com/alanmatzumiya/pySpectralPDE/blob/master/docs/presentation/presentation.pdf" width="100%" height="550px">
