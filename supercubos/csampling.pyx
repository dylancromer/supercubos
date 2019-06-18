import numpy as np
from _sampling import latin_sample as _sample




class LatinSampler:
    def sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size

        hypercube_bins = np.array([np.random.permutation(num_samples) for i in range(dim)])
        hypercube_bins = np.unique(hypercube_bins, axis=0)

        while hypercube_bins.shape[0] < dim:
            extra_point = np.random.permutation(num_samples)[None, :]
            hypercube_bins = np.concatenate((hypercube_bins, extra_point), axis=0)
            hypercube_bins = np.unique(hypercube_bins, axis=0)

        lengths = param_maxes - param_mins

        hypercube_points = lengths*(hypercube_bins.T + 0.5)/num_samples

        return hypercube_points

    def sample_cython(self, param_mins, param_maxes, num_samples):
        return _sample(param_mins, param_maxes, num_samples)
