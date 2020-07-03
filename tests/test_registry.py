"""Test the module can be imported."""

import unittest
from dasher.registry_util import RegistryUtil

class TestRegistry(unittest.TestCase):
    """A test case for import tests."""

    def test_registry(self):
        """Test that a ttl registry can be loaded."""
        ru = RegistryUtil(local_path="data/ontologies.ttl")
        srcs = ru.sources()
        assert len(srcs) > 10
        for s in srcs:
            print(f'Src: {s.id} URL {s.url}')
