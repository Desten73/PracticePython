from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runnerfirst = Runner("Усейн", 10)
        self.runnersecond = Runner("Андрей", 9)
        self.runnerthird = Runner("Ник", 3)

    def tearDown(self):
        print(self.all_results)

    def testOne(self):
        tournament = Tournament(90, self.runnerfirst, self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == "Ник")

    def testTwo(self):
        tournament = Tournament(90, self.runnersecond, self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == "Ник")

    def testThree(self):
        tournament = Tournament(90, self.runnerfirst, self.runnersecond,
                                self.runnerthird)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3] == "Ник")

    def testWithWrong(self):
        tournament = Tournament(12, Runner("R1", 7),
                                Runner("R2", 8), Runner("R3", 10))
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3] == "R1")
