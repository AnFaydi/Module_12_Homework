from tests_12_1 import RunnerTest
from source_12_1 import Runner1
from tests_12_2 import TournamentTest, Runner, Tournament
from unittest import TestCase
import unittest

class RunnerTest(TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker_test = Runner1('obj_walk')
        for i in range(10):
            walker_test.walk()
        self.assertEqual(walker_test.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_test = Runner1('obj_run')
        for i in range(10):
            runner_test.run()
        self.assertEqual(runner_test.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        challenge_test_1 = Runner1('obj')
        challenge_test_2 = Runner1('obj2')
        for i in range(10):
            challenge_test_1.walk()
            challenge_test_2.run()
        self.assertNotEqual(challenge_test_1.distance, challenge_test_2.distance)

class TournamentTest(TestCase):
    is_frozen = True
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)
        self.runner_test = Runner('Тестовый бегун', 1)
    @classmethod
    def setUpClass(cls):
         cls.all_results = dict()

    @classmethod
    def tearDownClass(cls):
        """
        вывод all_results в столбик
        """
        for key, obj in TournamentTest.all_results.items():
            print('\n')
            for key_in, obj_in in obj.items():
                print(f"{key_in}: {obj_in.name}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first(self):
        usain_nik = Tournament(90, self.runner_1, self.runner_2)
        self.all_results['first_tour'] = usain_nik.start()
        self.assertTrue(self.all_results['first_tour'][2] == 'Андрей')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second(self):
        andrey_nik = Tournament(90, self.runner_2, self.runner_3)
        self.all_results['second_tour'] = andrey_nik.start()
        self.assertTrue(self.all_results['second_tour'][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third(self):
        usain_andrey_nik = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results['third_tour'] = usain_andrey_nik.start()
        self.assertTrue(self.all_results['third_tour'][3] == 'Ник')