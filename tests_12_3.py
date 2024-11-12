import unittest
from suite_12_3 import RunnerTest, TournamentTest, skip_if_frozen

# Создание объекта TestSuite и добавление тестов
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Запуск тестов
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
