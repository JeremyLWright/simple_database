import shutil
import unittest

from collections import defaultdict
from hypothesis import settings
import hypothesis.strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule

from SampleDatabaseFascade import SampleDatabaseFascade
from ModelDatabaseFascade import ModelDatabaseFascade

class DatabaseComparison(RuleBasedStateMachine):
    def __init__(self):
        super(DatabaseComparison, self).__init__()
        self.uut = SampleDatabaseFascade()
        self.model = ModelDatabaseFascade()

    keys = Bundle('keys')
    values = Bundle('values')

    @rule(target=keys, k=st.binary())
    def k(self, k):
        return k

    @rule(target=values, v=st.binary())
    def v(self, v):
        return v

    @rule(k=keys, v=values)
    def save(self, k, v):
        self.model.set(k, v)
        self.uut.set(k,v)

    #@rule(k=keys, v=values)
    #def delete(self, k, v):
    #    self.uut.delete(k)
    #    self.model.delete(k)

    @rule(k=keys)
    def values_agree(self, k):
        actual = self.uut.get(k)
        expected = self.model.get(k)
        print("{} == {}".format(expected, actual))
        assert expected == actual
        
    def teardown(self):
        pass
        #shutil.rmtree(self.tempd)

DatabaseComparison.TestCase.settings = settings(max_examples=500, stateful_step_count=200)
TestDbComparison = DatabaseComparison.TestCase

if __name__== '__main__':
    unittest.main()

