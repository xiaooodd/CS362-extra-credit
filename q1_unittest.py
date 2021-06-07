import unittest
import q1

class TestName(unittest.TestCase):
    def test1(self):
        self.assertEqual(q1.sen_rev("sen is tom"), "tom is sen")

    def test2(self):
        self.assertEqual(q1.sen_rev("I am Tom."), "Tom. am I")


if __name__ == '__main__':
    unittest.main(verbosity=2)