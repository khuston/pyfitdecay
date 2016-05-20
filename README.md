Kaufmann2003
pyfitdecay
============

Two Python implementations of fitting a sum of exponentials to numerical data.
I haven't tested both carefully, but method 2 seems to work better:

1. Based on Kaufmann (2003) "Fitting a Sum of Exponentials to Numerical Data".
2. Based on scipy.optimize differential evolution

**Note:** The `kaufmann` implementation finds the best fit assuming the exponential
_does not_ decay to zero, whereas the `diffevol` implementation _does_ assume the
exponential decays to zero.

##TODO
- add error analysis (note: proper error analysis would probably include basin hopping,
but 
- describe algorithm
