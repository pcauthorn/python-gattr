import unittest

from gattr.code import gattr

NESTED_DICT = {'k1': {'n1k1': 'n1v1'}}

NESTED_LIST = [[1, 1, 1], [2, 2, 2]]


class O:
    def __init__(self, v):
        self.attr = v

    def get_attr(self):
        return self.attr


NESTED_OBJ = O(O(O('value')))

MIXED = {'mk1': [O('mixedv')]}


class TestDict(unittest.TestCase):

    def test_existing(self):
        self.assertEqual(gattr(NESTED_DICT, 'k1', 'n1k1'), 'n1v1')

    def test_non_existing_is_none(self):
        self.assertIsNone(gattr(NESTED_DICT, 'notthere'))


class TestDefault(unittest.TestCase):

    def test_default(self):
        self.assertEqual(gattr(NESTED_DICT, 'notthere', default='default'), 'default')
        self.assertEqual(gattr(NESTED_DICT, 'k1', 'n1k1', default='hello'), 'n1v1')


class TestList(unittest.TestCase):

    def test_existing(self):
        self.assertEqual(gattr(NESTED_LIST, 0, 1), 1)
        self.assertEqual(gattr(NESTED_LIST, -1, 0), 2)

    def test_non_existing_is_none(self):
        self.assertIsNone(gattr(NESTED_LIST, 42))

    def test_error_returns_none(self):
        self.assertIsNone(gattr(NESTED_LIST, 'notthere'))


class TestObject(unittest.TestCase):

    def test_existing(self):
        self.assertEqual(gattr(NESTED_OBJ, 'get_attr', 'get_attr', 'get_attr', invoke_callables=True), 'value')
        self.assertEqual(gattr(NESTED_OBJ, 'attr', 'get_attr', 'attr', invoke_callables=True), 'value')
        self.assertEqual(gattr(NESTED_OBJ, 'attr', 'attr', 'attr'), 'value')

    def test_existing_without_kwarg(self):
        self.assertIsNone(gattr(NESTED_OBJ, 'get_attr', 'get_attr', 'get_attr'))

    def test_non_existing_is_none(self):
        self.assertIsNone(gattr(NESTED_OBJ, 'attr1', invoke_callables=True))


if __name__ == '__main__':
    unittest.main()
