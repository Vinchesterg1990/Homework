import unittest
import test_1

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rune = test_1.Runner('Белка')
        for i in range(10):
            rune.walk()
        self.assertEqual(rune.distance,50)

    def test_run(self):
        rune = test_1.Runner("Зайка")
        for i in range(10):
            rune.run()
        self.assertEqual(rune.distance, 100)

    def test_challenge(self):
        misha = test_1.Runner('Мишка')
        wolf = test_1.Runner('Волк')
        for i in range (10):
            misha.walk()
            wolf.run()
        self.assertNotEqual(misha.distance, wolf.distance)

if __name__ == "__main":
    unittest.main

