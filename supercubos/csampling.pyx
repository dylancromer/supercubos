cimport numpy as np
import numpy as np
ctypedef np.uint64_t npfloat




cdef np.ndarray[npfloat, ndim=2] latin_sample(np.ndarray[npfloat, ndim=1] param_mins,
                                              np.ndarray[npfloat, ndim=1] param_maxes,
                                              int num_samples):
    cdef int dim
    dim = param_mins.size

    cdef np.ndarray[npfloat, ndim=1] hypercube_bins
    hypercube_bins = np.array([np.random.permutation(num_samples) for i in range(dim)])
    hypercube_bins = np.unique(hypercube_bins, axis=0)

    cdef np.ndarray[npfloat, ndim=1] extra_point
    while hypercube_bins.shape[0] < dim:
        extra_point = np.random.permutation(num_samples)[None, :]
        hypercube_bins = np.concatenate((hypercube_bins, extra_point), axis=0)
        hypercube_bins = np.unique(hypercube_bins, axis=0)

    cdef np.ndarray[npfloat, ndim=1] lengths
    lengths = param_maxes - param_mins

    cdef np.ndarray[npfloat, ndim=2] hypercube_points
    hypercube_points = lengths*(hypercube_bins.T + 0.5)/num_samples

    return hypercube_points
