import unittest

from tasks import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci('dfghj')

        with self.assertRaises(ValueError):
            self.fibonacci(-53687)

    def test_performance(self):
        self.assertLessEqual(self.fibonacci(50), 425765675645)

    def test_fibonacci(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)
        self.assertEqual(self.fibonacci(15), 610)
        self.assertEqual(self.fibonacci(20), 6765)
        self.assertEqual(self.fibonacci(100), 354224848179261915075)
        self.assertEqual(self.fibonacci(200), 280571172992510140037611932413038677189525)


class TestFormatedName(unittest.TestCase):

    def test_incorrect_input(self):
        with self.assertRaises(TypeError):
            formatted_name(123, 'Ivanov', 'Petrov')
        with self.assertRaises(TypeError):
            formatted_name('Ivan', 123, 'Petrov')
        with self.assertRaises(TypeError):
            formatted_name('Ivan', 'Ivanov', 123)

    def test_first_last_name(self):
        formatted = formatted_name('Ivan', 'Ivanov')
        self.assertEqual(formatted, 'Ivan Ivanov')

    def test_first_middle_last_name(self):
        formatted = formatted_name('Anna', 'Sergeevna', 'Petrova')
        self.assertEqual(formatted, 'Anna Petrova Sergeevna')

    def test_first_empty_middle_last_name(self):
        formatted = formatted_name('Peter', 'Sidorov', '')
        self.assertEqual(formatted, 'Peter Sidorov')

    def test_all_lowercase_names(self):
        formatted = formatted_name('anna', 'ivanova')
        self.assertEqual(formatted, 'Anna Ivanova')

    def test_all_uppercase_names(self):
        formatted = formatted_name('MARIA', 'PETROVA')
        self.assertEqual(formatted, 'Maria Petrova')

    def test_mixed_case_names(self):
        formatted = formatted_name('IvAn', 'SmirnOv')
        self.assertEqual(formatted, 'Ivan Smirnov')

    def test_long_middle_name(self):
        formatted = formatted_name('Dmitry', 'Petrov', 'Aleksandrovich')
        self.assertEqual(formatted, 'Dmitry Aleksandrovich Petrov')


if __name__ == '__main__':
    unittest.main()
