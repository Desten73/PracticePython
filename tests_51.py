import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Max")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Dag")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runnerfirst = Runner("Max")
        runnersecond = Runner("Dag")
        for _ in range(10):
            runnerfirst.run()
            runnersecond.walk()
        self.assertNotEqual(runnerfirst.distance, runnersecond.distance)


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runnerfirst = Runner("Усейн", 10)
        self.runnersecond = Runner("Андрей", 9)
        self.runnerthird = Runner("Ник", 3)

    def tearDown(self):
        print(self.all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testOne(self):
        tournament = Tournament(90, self.runnerfirst, self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testTwo(self):
        tournament = Tournament(90, self.runnersecond, self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testThree(self):
        tournament = Tournament(90, self.runnerfirst, self.runnersecond,
                                self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testWithWrong(self):
        tournament = Tournament(12, Runner("R1", 7),
                                Runner("R2", 8), Runner("R3", 10))
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3] == "R1")
