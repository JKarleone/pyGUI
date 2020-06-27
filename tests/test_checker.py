from unittest import TestCase
from client.Checker import Checker


class TestAuth(TestCase):
    def test_empty_auth(self):
        self.assertEqual(Checker.check_auth('', ''), 'there are empty spaces')

    def test_empty_login(self):
        self.assertEqual(Checker.check_auth('', 'normalpass'), 'there are empty spaces')

    def test_empty_pass(self):
        self.assertEqual(Checker.check_auth('mylogin', ''), 'there are empty spaces')

    def test_normal_auth(self):
        self.assertEqual(Checker.check_auth('login', 'password'), '')


class TestReg(TestCase):
    def test_empty_reg(self):
        self.assertEqual(Checker.check_reg('', '', ''), 'there are empty spaces')

    def test_normal_reg(self):
        self.assertEqual(Checker.check_reg('mylogin', 'Sobolev', 'mypass123'), '')

    def test_reg_with_digit(self):
        self.assertEqual(Checker.check_reg('mylogin322', 'myname123', 'mypass321'), '')

    def test_reg_with_special_symbols(self):
        self.assertEqual(Checker.check_reg('mylogin?', 'myname&3', 'mypass&1'), 'there are invalid characters')


class TestFilm(TestCase):
    def test_empty_film(self):
        self.assertEqual(Checker.check_film('', '', '', '', ''), 'there are empty spaces')

    def test_normal_film(self):
        self.assertEqual(Checker.check_film('title', 'desc', '2020', 'Elon Musk, Ben Affleck', 'Leonardo DiCaprio'), '')

    def test_2_long_description(self):
        my_str = 'abc' * 43
        self.assertEqual(Checker.check_film('title', my_str, '2010', 'Elon Musk', 'Bill Gates'),
                         'description mustn\'t exceed 128 symbols')

    def test_2_many_actors(self):
        actors = 'Elon Musk, Leonardo DiCaprio, Ben Affleck, Johny Depp, Ryan Reynolds'
        self.assertEqual(Checker.check_film('title', 'desc', '2018', actors, 'Bondarchyk'), 'too many actors')

    def test_comma_filmmakers(self):
        filmmaker = 'Ben Affleck, Elon Musk'
        self.assertEqual(Checker.check_film('title', 'desc', '2018', 'actors', filmmaker),
                         'there should be the only one filmmaker')

    def test_space_filmmakers(self):
        filmmaker = 'Ben Affleck Elon Musk'
        self.assertEqual(Checker.check_film('title', 'desc', '2018', 'actors', filmmaker),
                         'there should be the only one filmmaker')

    def test_normal_date(self):
        self.assertEqual(Checker.check_film('title', 'desc', '2018', 'actors', 'Elon'), '')

    def test_negative_year(self):
        self.assertEqual(Checker.check_film('title', 'desc', '-2018', 'actors', 'Elon'), 'wrong year')

    def test_non_year(self):
        self.assertEqual(Checker.check_film('title', 'desc', 'hi', 'actors', 'Elon'), 'wrong year')

    def test_non_real_date(self):
        self.assertEqual(Checker.check_film('title', 'desc', '988', 'actors', 'Elon'), 'date is impossible')
        self.assertEqual(Checker.check_film('title', 'desc', '2077', 'actors', 'Elon'), 'date is impossible')

    def test_ampersand(self):
        self.assertEqual(Checker.check_film('title', 'desc', '2009', 'actors', 'Elon&Ben'), 'there are invalid symbols')
