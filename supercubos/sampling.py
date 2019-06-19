import numpy as np




class TooFewSamplesError(Exception):
    pass


class LatinSampler:
    def get_lh_sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size

        latin_points = np.array([np.random.permutation(num_samples) for i in range(dim)]).T

        lengths = param_maxes - param_mins
        latin_points = lengths*(latin_points + 0.5)/num_samples

        return latin_points

    def get_sym_sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size

        even_nums = np.arange(0, num_samples, 2)
        permutations = np.array([np.random.permutation(even_nums) for i in range(dim)])
        inverses = (num_samples - 1) - permutations

        return np.concatenate((permutations,inverses), axis=1).T
