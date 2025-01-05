from source_12_1 import Runner
from unittest import TestCase
import unittest

class RunnerTest(TestCase):
    def test_walk(self):
        walker_test = Runner('obj_walk')
        for i in range(10):
            walker_test.walk()
        self.assertEqual(walker_test.distance, 50)

    def test_run(self):
        runner_test = Runner('obj_run')
        for i in range(10):
            runner_test.run()
        self.assertEqual(runner_test.distance, 100)
    def test_challenge(self):

        challenge_test_1 = Runner('obj')
        challenge_test_2 = Runner('obj2')
        for i in range(10):
            challenge_test_1.walk()
            challenge_test_2.run()
        self.assertNotEqual(challenge_test_1.distance, challenge_test_2.distance)
