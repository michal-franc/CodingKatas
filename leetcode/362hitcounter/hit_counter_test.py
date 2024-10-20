import unittest
from hit_counter import HitCounter 

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        expected = 3
        hitCounter = HitCounter()
        hitCounter.hit(1)
        hitCounter.hit(2)
        hitCounter.hit(3)
        actual = hitCounter.getHits(4)
        self.assertEqual(actual, expected)

    def test_example2(self):
        expected = 3
        hitCounter = HitCounter()
        hitCounter.hit(1)
        hitCounter.hit(2)
        hitCounter.hit(3)
        hitCounter.hit(300)
        actual = hitCounter.getHits(301)
        self.assertEqual(actual, expected)

    def test_example3(self):
        expected = 8
        hitCounter = HitCounter()
        hitCounter.hit(1)
        hitCounter.hit(2)
        hitCounter.hit(3)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        actual = hitCounter.getHits(301)
        self.assertEqual(actual, expected)

    def test_example4(self):
        expected = 6
        hitCounter = HitCounter()
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(300)
        hitCounter.hit(900)
        hitCounter.hit(900)
        hitCounter.hit(900)
        hitCounter.hit(900)
        hitCounter.hit(900)
        hitCounter.hit(900)
        actual = hitCounter.getHits(1000)
        self.assertEqual(actual, expected)
