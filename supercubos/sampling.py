import numpy as np




class TooFewSamplesError(Exception):
    pass


class LatinSampler:
    def _check_numerical_sanity(self, dim, num_samples):
        if np.math.factorial(num_samples) < dim:
            raise TooFewSamplesError("The number of samples is too small"
                                     " for the given dimension")

    def get_lh_sample(self, param_mins, param_maxes, num_samples, normalize=True):
        dim = param_mins.size

        self._check_numerical_sanity(dim, num_samples)

        hypercube_bins = np.array([np.random.permutation(num_samples) for i in range(dim)])
        hypercube_bins = np.unique(hypercube_bins, axis=0)

        while hypercube_bins.shape[0] < dim:
            extra_point = np.random.permutation(num_samples)[None, :]
            hypercube_bins = np.concatenate((hypercube_bins, extra_point), axis=0)
            hypercube_bins = np.unique(hypercube_bins, axis=0)

        if normalize:
            lengths = param_maxes - param_mins
            hypercube_points = lengths*(hypercube_bins.T + 0.5)/num_samples

        return hypercube_points


class SymmetricSampler(LatinSampler):
    def get_sym_sample(self, param_mins, param_maxes, num_samples):
        initial_samples = self.get_lh_sample(param_mins, param_maxes, num_samples/2, normalize=False)

        return initial_samples
