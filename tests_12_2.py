from unittest import TestCase
import unittest

class Runner:
    def __init__(self, name, speed=5): # объекту дается имя, дистанция и скорость(5)
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2 #метод бежать

    def walk(self):
        self.distance += self.speed # метьод идти

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str): # если сравнение объекта со строкой
            return self.name == other
        elif isinstance(other, Runner): # если сравнение объекта с объектом класса бегун
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    continue

        return finishers

class TournamentTest(TestCase):
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
    def test_first(self):
        usain_nik = Tournament(90, self.runner_1, self.runner_2)
        self.all_results['first_tour'] = usain_nik.start()
        self.assertTrue(self.all_results['first_tour'][2] == 'Андрей')

    def test_second(self):
        andrey_nik = Tournament(90, self.runner_2, self.runner_3)
        self.all_results['second_tour'] = andrey_nik.start()
        self.assertTrue(self.all_results['second_tour'][2] == 'Ник')

    def test_third(self):
        usain_andrey_nik = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results['third_tour'] = usain_andrey_nik.start()
        self.assertTrue(self.all_results['third_tour'][3] == 'Ник')