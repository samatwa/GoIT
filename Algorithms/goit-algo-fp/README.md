# goit-algo-fp

## Monte Carlo calculation accuracy

Monte Carlo simulation estimates probabilities by sampling random processes. This experiment estimates the distribution of the sum of two six-sided dice.

## Results

The recorded Monte Carlo and analytical probabilities are:

| Sum | Monte Carlo Probability | Analytical Probability |
|:---:|:-----------------------:|:----------------------:|
|  2  |          0.0278         |         0.0278         |
|  3  |          0.0552         |         0.0556         |
|  4  |          0.0832         |         0.0833         |
|  5  |          0.1113         |         0.1111         |
|  6  |          0.1388         |         0.1389         |
|  7  |          0.1672         |         0.1667         |
|  8  |          0.1392         |         0.1389         |
|  9  |          0.1111         |         0.1111         |
| 10  |          0.0837         |         0.0833         |
| 11  |          0.0550         |         0.0556         |
| 12  |          0.0276         |         0.0278         |

The simulation used 1,000,000 trials. Its probabilities closely match the analytical distribution, with small differences caused by finite random sampling and numerical precision. The observed agreement supports this implementation for the tested experiment. Monte Carlo methods are useful when an analytical calculation is difficult or unavailable.
