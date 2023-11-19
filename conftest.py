import pytest
from main import BooksCollector


@pytest.fixture
def fill_books_genre():
    book_genre = {'Жил-был пёс': 'Мультфильмы', 'Властелин колец': 'Фантастика', 'Десять негритят': 'Детективы',
                  'Колобок': 'Мультфильмы', 'Один дома': 'Комедии', 'Оно': 'Ужасы'}
    collector = BooksCollector()
    collector.books_genre.update(book_genre)
    return collector
