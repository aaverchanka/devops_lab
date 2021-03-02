from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""
        self.mock_expected_result = {'num': 444, 'title': 'title', 'link': 'its my mock link'}
        self.mock_html = {'html': {'href': 'its my mock link'}}

    def test_parse_response_item(self):
        """Test should return correct parsed object"""
        mock_item_dict = {'number': 444, 'title': 'title', '_links': self.mock_html}
        result = pulls.parse_response_item(mock_item_dict)
        self.assertEqual(result, self.mock_expected_result)

    def test_get_open_close_events(self):
        """Test should return correct array for open or closed events"""
        result = pulls.get_open_close_events('open', self.get_mock_response)
        self.assertEqual(result, [self.mock_expected_result])

    def test_get_accept_need_work_events(self):
        """Test should return correct array for accept or need work events"""
        result = pulls.get_accept_need_work_events('need works', self.get_mock_response)
        self.assertEqual(result, [self.mock_expected_result])

    def tearDown(self):
        """Finish"""

    def get_mock_response(self, params):
        mock_label = {'name': 'need works'}
        mock_item_dict = {'number': 444, 'title': 'title', '_links\
                            ': self.mock_html, 'labels': [mock_label]}
        return [mock_item_dict]
