import random
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

        unused_values = [np.random.permutation(num_samples).astype(set) for i in range(dim)]
        for i in range(dim):
            randomized_permutation = random.shuffle(

            unused_values
        latin_points = np.zeros((dim, num_samples), dtype=int)

        for i in range(0, num_samples, 2):
            point1 = np.empty(dim)
            point2 = np.empty(dim)

            for j in range(dim):
                value = unused_values[i][j]
                point1[j] = value
                unused_values[j].remove(value)

                inverse = (num_samples - 1) - value
                point2[j] = inverse
                unused_values[j].remove(inverse)

            latin_points[:, i] = point1
            latin_points[:, i+1] = point2

        return latin_points.T
