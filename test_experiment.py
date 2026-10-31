import unittest
from experiment import simulate


class CacheTests(unittest.TestCase):
    def test_reuse(self):
        self.assertEqual(simulate([1, 2, 1, 2], 2), (2, 2))

    def test_scan_thrashes(self):
        self.assertEqual(simulate(list(range(8)) * 2, 4), (0, 16))

    def test_lru_eviction(self):
        self.assertEqual(simulate([1, 2, 1, 3, 2], 2), (1, 4))

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            simulate([1], 0)


if __name__ == "__main__":
    unittest.main()
