import unittest

from gh_template_py import run_gh_template_py


class TestCase(unittest.TestCase):

    def test_dump(self):
        self.assertTrue(run_gh_template_py._run())


if __name__ == '__main__':
    unittest.main()
