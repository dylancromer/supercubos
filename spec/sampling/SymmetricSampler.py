import pytest
import numpy as np
from supercubos.sampling import SymmetricSampler




def describe_symmetric_sampler():

    def describe_get_sym_sample():

        @pytest.fixture
        def sampler():
            return SymmetricSampler()

        def it_works_for_a_trivial_case(sampler):
            dim = 2
            nsamps = 6

            param_mins = np.zeros(dim)
            param_maxes = nsamps*np.ones(dim)

            lh_samples = sampler.get_sym_sample(param_mins, param_maxes, nsamps)

            for samp in lh_samples:
                reflection = nsamps - samp
                assert any((lh_samples[:] == reflection).all(axis=1))

        def it_requires_an_even_number_of_samples(sampler):
            pass
