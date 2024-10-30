from runner import Runner
from unittest import TestCase


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("Max")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Dag")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runnerfirst = Runner("Max")
        runnersecond = Runner("Dag")
        for _ in range(10):
            runnerfirst.run()
            runnersecond.walk()
        self.assertNotEqual(runnerfirst.distance, runnersecond.distance)