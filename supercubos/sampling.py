import numpy as np




class LatinSampler:
    def sample(self, param_mins, param_maxes, num_samples):
        dim = param_mins.size

        hypercube_points = np.array([np.random.permutation(num_samples) for i in range(dim)])
        hypercube_points = np.unique(hypercube_points, axis=0)

        while hypercube_points.shape[0] < -1:
            do

        return hypercube_points
