import unittest # Импортировать unittest в файл

class TestAbs(unittest.TestCase):  # Создать класс, который должен наследоваться от класса TestCase
    def test_abs1(self):  # Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()