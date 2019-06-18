import cython
cimport numpy as np
import numpy as np
ctypedef np.double_t npfloat




@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.ndarray[npfloat, ndim=2] _latin_sample(np.ndarray[npfloat, ndim=1] param_mins,
                                               np.ndarray[npfloat, ndim=1] param_maxes,
                                               int num_samples):
    cdef int dim
    dim = param_mins.size

    cdef np.ndarray[npfloat, ndim=2] hypercube_bins
    hypercube_bins = np.array([np.random.permutation(num_samples).astype(np.double) for i in range(dim)])
    hypercube_bins = np.unique(hypercube_bins, axis=0)

    cdef np.ndarray[npfloat, ndim=2] extra_point
    while hypercube_bins.shape[0] < dim:
        extra_point = np.random.permutation(num_samples).astype(np.double)[None, :]
        hypercube_bins = np.concatenate((hypercube_bins, extra_point), axis=0)
        hypercube_bins = np.unique(hypercube_bins, axis=0)

    cdef np.ndarray[npfloat, ndim=1] lengths
    lengths = param_maxes - param_mins

    cdef np.ndarray[npfloat, ndim=2] hypercube_points
    hypercube_points = lengths*(hypercube_bins.T + 0.5)/num_samples

    return hypercube_points


def latin_sample(np.ndarray[npfloat, ndim=1] param_mins,
                 np.ndarray[npfloat, ndim=1] param_maxes,
                 int num_samples):
    return _latin_sample(param_mins, param_maxes, num_samples)
