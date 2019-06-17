import pytest
import numpy as np
from supercubos.sampling import LatinSampler




def describe_latin_sampler():

    def describe_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def it_works_for_a_trivial_case(sampler):
            param_mins = np.zeros(3)
            param_maxes = np.ones(3)

            lh_samples = sampler.sample(param_mins, param_maxes, 2)

            assert False, lh_samples.shape

            assert (lh_samples[0,0] == 0.25) or (lh_samples[0,0] == 0.75)

        def it_works_for_a_simple_case(sampler):
            param_mins = np.zeros(3)
            param_maxes = 3*np.ones(3)

            lh_samples = sampler.sample(param_mins, param_maxes, 3)

            #assert lh_samples[0,0] in {0.5, 1.5, 2.5}
