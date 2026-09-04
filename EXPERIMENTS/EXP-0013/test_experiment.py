import unittest
from experiment import run

class TestEXP0013(unittest.TestCase):
    def test_deterministic(self):
        for mode in ('B','C','D'):
            self.assertEqual(run(7, mode), run(7, mode))
    def test_same_seed_has_same_structure(self):
        for mode in ('B','C','D'):
            r = run(3, mode)
            self.assertIsNotNone(r.adaptation)
            self.assertGreaterEqual(r.revisions, 0)
            self.assertGreaterEqual(r.false_switches, 0)

if __name__ == '__main__':
    unittest.main()
