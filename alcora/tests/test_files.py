import unittest


class TestFilesMethods(unittest.TestCase):
    def test_count_by_ext_nondir(self):
        """
        If path is not a directory, return 0.
        """
        from alcora.files import count_by_extension

        self.assertEqual(count_by_extension("foo", ".py"), 0)


if __name__ == '__main__':
    unittest.main()
