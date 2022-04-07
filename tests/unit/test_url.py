from is_ipfs import Validator
import unittest
import tests.testing_data as testing_data


class TestCase(unittest.TestCase):
    def test_ipfs_url(self):
        with self.subTest("Test valid IPFS URL entries from fixtures"):
            for entry in testing_data.valid_entries["url"]["ipfs"]:
                print(entry)
                self.assertTrue(Validator(entry)._is_ipfs_url())

        with self.subTest("Test invalid IPFS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_ipfs_url())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
