import pytest


@pytest.fixture
def fill_books_genre():
    book_genre = {'Жил-был пёс': 'Мультфильмы', 'Властелин колец': 'Фантастика', 'Десять негритят': 'Детективы',
                  'Колобок': 'Мультфильмы', 'Один дома': 'Комедии', 'Оно': 'Ужасы'}
    return book_genre
