# goit-algo-hw-10

## Monte Carlo integration

This task implements definite integration with Monte Carlo sampling and compares the result with `scipy.integrate.quad`.

| Number of points | Monte Carlo integral | quad integral | Absolute difference |
|---:|---:|---:|---:|
| 10000 | 2.6951575965113133 | 2.666666666666667 | 0.028490929844646296 |
| 100000 | 2.671886515825384 | 2.666666666666667 | 0.005219849158716983 |

In these runs, increasing `num_points` produced a closer estimate. Small deviations are expected because sampling is random; convergence does not guarantee that every larger individual sample has a smaller error.

Monte Carlo integration can also be useful for multidimensional integrals or cases where an analytical solution is difficult.
