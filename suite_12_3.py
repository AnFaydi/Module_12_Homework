import unittest
import tests_12_3
my_case = unittest.TestSuite()
my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

run_case = unittest.TextTestRunner(verbosity=2)
run_case.run(my_case)