import pytest
import numpy as np
from supercubos import LatinSampler


def describe_latin_sampler():

    def describe_get_lh_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def it_works_for_a_trivial_case(sampler):
            param_mins = np.zeros(2)
            param_maxes = np.ones(2)

            lh_samples = sampler.get_lh_sample(param_mins, param_maxes, 2)

            assert (lh_samples[0,0] == 0.25) or (lh_samples[0,0] == 0.75)
            assert lh_samples.shape == (2,2)

        def it_works_for_a_simple_case(sampler):
            param_mins = np.zeros(2)
            param_maxes = 3*np.ones(2)

            lh_samples = sampler.get_lh_sample(param_mins, param_maxes, 3)

            assert lh_samples[0,0] in {0.5, 1.5, 2.5}
            assert lh_samples.shape == (3, 2)

        def you_can_change_the_rng():
            sampler = LatinSampler(rng=np.random.default_rng(seed=13))
            param_mins = np.zeros(2)
            param_maxes = np.ones(2)

            lh_samples = sampler.get_lh_sample(param_mins, param_maxes, 2)
            assert lh_samples[0,0] == 0.75
            assert lh_samples.shape == (2,2)

    def describe_get_sym_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def it_works_for_a_trivial_case(sampler):
            dim = 2
            nsamps = 6

            param_mins = np.zeros(dim)
            param_maxes = nsamps*np.ones(dim)

            lh_samples = sampler.get_sym_sample(param_mins, param_maxes, nsamps)

            for samp in lh_samples:
                reflection = nsamps - samp
                assert any((lh_samples[:] == reflection).all(axis=1))

    def describe_get_rand_sample():

        @pytest.fixture
        def sampler():
            return LatinSampler()

        def it_works(sampler):
            dim = 2
            nsamps = 6

            param_mins = np.zeros(dim)
            param_maxes = nsamps*np.ones(dim)

            lh_samples = sampler.get_rand_sample(param_mins, param_maxes, nsamps)

            assert np.all(lh_samples >= param_mins)
            assert np.all(lh_samples <= param_maxes)
