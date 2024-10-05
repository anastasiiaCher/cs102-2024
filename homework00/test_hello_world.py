"""Программа проверки работы"""

import unittest

import hello_world


class HelloTestCase(unittest.TestCase):
    """Создание класса HelloTestCase"""
    def test_hello(self):
        """Функция по проверке вывода"""
        m = "message"
        self.assertEqual(m, hello_world.text())
