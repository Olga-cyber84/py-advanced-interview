import unittest
from parameterized import parameterized
from app import show_document_info, add_new_doc, delete_doc, check_document_existance
from unittest.mock import patch, Mock


class TestSecretaryProgram(unittest.TestCase):
    # проверка функции по получению информации о документах
    @parameterized.expand([
        ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
         'passport : 2207 876234 : Василий Гупкин'),
        ({'type': 'invoice', 'number': '', 'name': 'Геннадий Покемонов'},
         'invoice :  : Геннадий Покемонов')
    ])
    def test_show_document_info(self, document, result):
        checking_doc = show_document_info(document)
        self.assertEqual(checking_doc, result)
        self.assertIsInstance(checking_doc, str)

    # проверка функции добавления
    @parameterized.expand([
        (['1001', 'passport', 'Bob', '10'], '10'),
        (['1001', 'passport', 'Bob', '-10'], '10'),
        (['1001', 'passport', 'Bob', '0'], 'такой полки не существует')
    ])
    @patch('builtins.input')
    def test_add_new_doc(self, checking, result, input):
        input.side_effect = checking
        checking_doc_shelf_number = add_new_doc()
        self.assertEqual(checking_doc_shelf_number, result)
        self.assertIsInstance(checking_doc_shelf_number, str)

    # проверка функции удаления элементов из словаря
    @parameterized.expand([
        ('2207 876234', True),
        ('11-5', False),
        ('10006', True),
        ('10006.', False),
        ('-10006', True)
    ])
    @patch('builtins.input')
    def test_delete_doc(self, checking, result, input):
        input.return_value = checking
        checking_doc = delete_doc()
        self.assertEqual(checking_doc[1], result)
        self.assertIsInstance(checking_doc[1], bool)


if __name__ == '__main__':
    unittest.main()
