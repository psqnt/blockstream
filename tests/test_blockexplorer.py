import unittest

from blockstream import blockexplorer, util

class Tests(unittest.TestCase):

    def test_api_call(self):
        response = util.call_api('blocks/')
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)


if __name__ == "__main__":
    unittest.main()
