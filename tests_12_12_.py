import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        i = 1
        while self.distance > 0:
            for runner in self.runners:
                if self.distance > 0:
                    runner.run()
                    self.distance -= runner.speed * 2
                    if self.distance <= 0:
                        results[i] = runner.name
                        i += 1
        return results

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        self.all_results[1] = tournament.start()
        self.assertTrue(max(self.all_results[1], key=self.all_results[1].get) == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        self.all_results[2] = tournament.start()
        self.assertTrue(max(self.all_results[2], key=self.all_results[2].get) == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        self.all_results[3] = tournament.start()
        self.assertTrue(max(self.all_results[3], key=self.all_results[3].get) == "Ник")

if __name__ == '__main__':
    unittest.main()
