import numpy as np


class LatinSampler:
    def _check_num_is_even(self, num):
        if num % 2 != 0:
            raise ValueError("Number of samples must be even")

    def get_lh_sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size

        latin_points = np.array([np.random.permutation(num_samples) for i in range(dim)]).T

        lengths = (param_maxes - param_mins)[None, :]
        return lengths*(latin_points + 0.5)/num_samples + param_mins[None, :]

    def get_sym_sample(self, param_mins, param_maxes, num_samples):
        self._check_num_is_even(num_samples)

        dim = param_mins.size

        even_nums = np.arange(0, num_samples, 2)
        permutations = np.array([np.random.permutation(even_nums) for i in range(dim)])
        inverses = (num_samples - 1) - permutations

        latin_points = np.concatenate((permutations,inverses), axis=1).T

        lengths = (param_maxes - param_mins)[None, :]
        return  lengths*(latin_points + 0.5)/num_samples + param_mins[None, :]

    def get_rand_sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size
        lengths = param_maxes - param_mins
        return lengths[None, :]*np.random.rand(num_samples, dim) + param_mins[None, :]
