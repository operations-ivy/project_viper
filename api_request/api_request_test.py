import unittest
import requests_mock

from api_request import ApiRequest

class TestApiRequest(unittest.TestCase):

    @requests_mock.mock()
    def test_get_random(self):
        mock_response = {
            "categories": [],
            "created_at": "2020-01-05 13:42:19.576875",
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "id": "5Qr5w0WuQJ2YQlGm0p1h6w",
            "updated_at": "2020-01-05 13:42:19.576875",
            "url": "https://api.chucknorris.io/jokes/5Qr5w0WuQJ2YQlGm0p1h6w",
            "value": "Chuck Norris can make a snowman out of rain."
        }
        api = ApiRequest()
        self.assertTrue(api.get_random()["value"])


if __name__ == '__main__':
    unittest.main()