import pytest
import numpy as np
from supercubos.sampling import LatinSampler




def describe_latin_sampler_speed():

    def describe_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def sampling_is_fast(sampler, benchmark):
            param_mins = np.zeros(10)
            param_maxes = np.ones(10)
            nsamps = 10000

            benchmark(sampler.sample, param_mins, param_maxes, nsamps)

    def describe_sample_cython():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def cython_sampling_is_faster(sampler, benchmark):
            param_mins = np.zeros(10)
            param_maxes = np.ones(10)
            nsamps = 10000

            benchmark(sampler.sample_cython, param_mins, param_maxes, nsamps)
