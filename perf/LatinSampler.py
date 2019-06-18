import pytest
import numpy as np
from supercubos.sampling import LatinSampler




def describe_latin_sampler_speed():

    def describe_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def sampling_is_fast_for_10_dims_10000_samples(sampler, benchmark):
            param_mins = np.zeros(10)
            param_maxes = np.ones(10)
            nsamps = 10000

            benchmark(sampler.sample, param_mins, param_maxes, nsamps)
