import unittest

from def_result.ResultDetail import ResultDetail


class TestResultDetail(unittest.TestCase):
    def test_init_without_optional_args(self):
        title = 'title'
        result_detail = ResultDetail(title=title)

        self.assertEqual(result_detail.title, title)
        self.assertIsNone(result_detail.message)
        self.assertIsNone(result_detail.code)
        self.assertIsNotNone(result_detail.more_data)
        self.assertEqual(len(result_detail.more_data), 0)

    def test_init_with_optional_args(self):
        result_detail = ResultDetail(title='title', message='message', code=100, more_data=["more data"])

        self.assertEqual(result_detail.title, 'title')
        self.assertEqual(result_detail.message, 'message')
        self.assertEqual(result_detail.code, 100)

        self.assertIsNotNone(result_detail.more_data)
        self.assertEqual(len(result_detail.more_data), 1)
        self.assertEqual(result_detail.more_data[0], "more data")

    def test_is_instance_of(self):
        test_detail = FakeDetail("title")

        self.assertTrue(test_detail.is_instance_of(FakeDetail))
        self.assertTrue(test_detail.is_instance_of(ResultDetail))

    def test_add_more_data(self):
        result_detail = ResultDetail(title='title')
        result_detail.more_data = None  # We use none to make sure that our function does not run into problems.

        result_detail.add_more_data("more data")

        self.assertIsNotNone(result_detail.more_data)
        self.assertEqual(len(result_detail.more_data), 1)
        self.assertEqual(result_detail.more_data[0], "more data")

    def test_str_without_args(self):
        result_detail = ResultDetail(title='title')
        expected = "Title: title\n"

        self.assertEqual(str(result_detail), expected)

    def test_str_with_args(self):
        result_detail = ResultDetail(title='title', message='message', code=100)
        expected = "Title: title\nMessage: message\nCode: 100\n"

        self.assertEqual(str(result_detail), expected)


class FakeDetail(ResultDetail):
    pass


if __name__ == "__main__":
    unittest.main()
