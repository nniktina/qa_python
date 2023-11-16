from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Биба')
        collector.add_new_book('Боба')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_added_book_has_no_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_set_cartoon(self):
        collector = BooksCollector()
        collector.add_new_book('Жил-был пёс')
        collector.set_book_genre('Жил-был пёс', 'Мультфильмы')
        assert collector.get_book_genre('Жил-был пёс') == 'Мультфильмы'

    def test_get_book_genre_get_comedy(self, fill_books_genre):
        collector = BooksCollector()
        collector.books_genre.update(fill_books_genre)
        assert collector.get_book_genre('Один дома') == 'Комедии'

    def test_get_books_with_specific_genre_get_two_cartoons(self, fill_books_genre):
        collector = BooksCollector()
        collector.books_genre.update(fill_books_genre)
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Жил-был пёс', 'Колобок']

    def test_get_books_genre_get_all_dictionary(self, fill_books_genre):
        collector = BooksCollector()
        collector.books_genre.update(fill_books_genre)
        assert collector.get_books_genre() == {
        'Жил-был пёс': 'Мультфильмы',
        'Властелин колец': 'Фантастика',
        'Десять негритят': 'Детективы',
        'Колобок': 'Мультфильмы',
        'Один дома': 'Комедии',
        'Оно': 'Ужасы'
    }

    def test_get_books_for_children_return_four(self, fill_books_genre):
        collector = BooksCollector()
        collector.books_genre.update(fill_books_genre)
        assert collector.get_books_for_children() == ['Жил-был пёс', 'Властелин колец', 'Колобок', 'Один дома']

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Котенок по имени Гав')
        collector.add_book_in_favorites('Котенок по имени Гав')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one(self):
        collector = BooksCollector()
        collector.favorites.append('Дюна')
        collector.favorites.append('Игра престолов')
        collector.delete_book_from_favorites('Дюна')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_list_of_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Гарри Поттер и тайная комната')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и тайная комната')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень', 'Гарри Поттер и тайная комната']
