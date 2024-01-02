import unittest

from api_request import ApiRequest

class TestApiRequest(unittest.TestCase):
    def test_return_foo(self):
        api_request = ApiRequest()
        self.assertEqual(api_request.return_foo("bar"), "bar is the foo value")
        self.assertEqual(api_request.return_foo(""), " is the foo value")


if __name__ == '__main__':
    unittest.main()