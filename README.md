# supercubos
Generate Latin hypercubes in Python

`supercubos` is a module for computing [Latin Hypercube samples](https://en.wikipedia.org/wiki/Latin_hypercube_sampling) for interpolation. 

The basic idea is that one wants to evaluate some function, but the function takes a long time to calculate; longer than evaluating an interpolation of the same function. Thus to boost the speed of evaluation (perhaps for evaluating a Likelihood), you pre-calculate the function over some points, then solve the interpolation problem for those points (perhaps using radial basis functions or Gaussian process interpolation). This can then be used to evaluate the function at any point inside the range of the samples.

The hitch is that RBF/GP interpolation is an O(n^2) problem with respect to memory, limiting the number of sample points severely. This is especially problematic in higher dimensional cases, such as those where you are sampling a model with 4 or more parameters. In this case sampling on a grid is not feasible and people often turn to random sampling of points.

Random sampling has the downside that for small sample sizes, there is often signficant clustering of samples, which is not ideal for interpolation since clustered samples can be wasteful. Instead, often a better option is to use a Latin hypercube, which enforces a condition that sample bins may not share the same coordinates for *any* coordinate axis.
