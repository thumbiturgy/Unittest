import unittest
from join_me import join_me

class Test_Join_Me(unittest.TestCase):
    def test_join_me(self):
        actual = join_me(['steve', 'rick', 'al', 'betty'])
        expected = "Steve, Rick, Al, Betty, and me"
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
