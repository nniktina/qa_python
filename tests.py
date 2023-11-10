from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre.keys()) == 2

    def test_add_new_book_added_book_has_no_genre_true(self): #у добавленной книги нет жанра
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_set_cartoon(self): # устанавливаем книге жанр
        collector = BooksCollector()
        collector.add_new_book('Жил-был пёс')
        collector.set_book_genre('Жил-был пёс', 'Мультфильмы')
        assert collector.books_genre['Жил-был пёс'] == 'Мультфильмы'

    def test_get_book_genre_check_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома')
        collector.set_book_genre('Один дома', 'Комедии')
        assert collector.get_book_genre('Один дома') == 'Комедии'

    def test_get_books_with_specific_genre_get_cartoons(self):
        collector = BooksCollector()
        collector.add_new_book('Жил-был пёс')
        collector.add_new_book('Том и Джерри')
        collector.add_new_book('Пятый элемент')
        collector.set_book_genre('Жил-был пёс', 'Мультфильмы')
        collector.set_book_genre('Том и Джерри', 'Мультфильмы')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Жил-был пёс', 'Том и Джерри']

    def test_get_books_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Пятый элемент')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.set_book_genre('Пятый элемент', 'Фантастика')
        assert collector.get_books_genre() == {'Десять негритят':'Детективы', 'Пятый элемент':'Фантастика'}

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Котенок по имени Гав')
        collector.add_book_in_favorites('Котенок по имени Гав')
        assert 'Котенок по имени Гав' in collector.favorites
