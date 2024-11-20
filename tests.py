from main import BooksCollector
import pytest


class TestBooksCollector:

    # 1 Positive test of method "__init__" for genre
    def test_all_genres_true(self):
        books_collector = BooksCollector()
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # 2 Positive test of method "__init__" for genre age rating
    def test_genre_age_rating_true(self):
        books_collector = BooksCollector()
        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    # 3 Positive test of method "add_new_book"
    def test_add_new_book_correct_dict(self):
        books_collector = BooksCollector()
        book_name = 'The Great Gatsby'

        books_collector.add_new_book(book_name)

        assert books_collector.books_genre[book_name] == ''

    # 4 First negative test of method "add_new_book"
    @pytest.mark.parametrize('book_name', ['', 'nnmdnmd mdnmdnmdnmdnmdnmdn dnmdnmdnmdnmdn'])
    def test_add_new_book_length_more_than40_or_equal_zero_empty_list(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 0

    # 5 Second negative test of method "add_new_book"
    @pytest.mark.parametrize('book_name', ['The Lost', 'Fast & Furious'])
    def test_add_new_book_repeating_book_name_twice(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 1

    # 6 Positive test of method "set_book_genre"
    def test_set_book_genre_existing_book_name_and_existing_genre(self):
        books_collector = BooksCollector()
        book_name = 'Lord of the Rings'
        book_genre = 'Фантастика'

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.books_genre[book_name] == book_genre

    # 7 Positive test of method "get_book_genre" (exist genre)
    def test_get_book_genre_exist_correct_true(self):
        books_collector = BooksCollector()
        book_name = 'Lord of the Rings'
        book_genre = 'Фантастика'

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.get_book_genre(book_name) == book_genre

    # 8 Positive test of method "get_book_genre" (no genre exists)
    def test_get_book_genre_do_not_exist_correct(self):
        books_collector = BooksCollector()
        book_name = 'Lord of the Rings'

        books_collector.add_new_book(book_name)

        assert books_collector.get_book_genre(book_name) == ''

    # 9 Positive test of method "get_books_with_specific_genre"
    def test_get_books_with_specific_genre_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_name_2 = 'Star Wars'
        book_name_3 = 'Saw'
        book_genre_1 = 'Фантастика'
        book_genre_2 = 'Ужасы'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)
        books_collector.set_book_genre(book_name_2, book_genre_1)
        books_collector.set_book_genre(book_name_3, book_genre_2)

        assert books_collector.get_books_with_specific_genre(book_genre_1) == [book_name_1, book_name_2]

    # 10 Positive test of method "get_books_genre"
    def test_get_books_genre_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_genre_1 = 'Фантастика'
        book_name_2 = 'Saw'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)

        assert books_collector.get_books_genre() == {book_name_1: book_genre_1,
                                                     book_name_2: ''}

    # 11 Positive test of method "get_books_for_children"
    def test_get_books_for_children_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_genre_1 = 'Фантастика'
        book_name_2 = 'Saw'
        book_genre_2 = 'Ужасы'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.set_book_genre(book_name_1, book_genre_1)
        books_collector.set_book_genre(book_name_2, book_genre_2)

        assert books_collector.get_books_for_children() == [book_name_1]

    # 12 Positive test of method "add_book_in_favorites"
    def test_add_book_in_favorites_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_name_2 = 'Saw'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_2)

        assert books_collector.favorites == [book_name_2]

    # 13 Positive test of method "delete_book_from_favorites"
    def test_delete_book_from_favorites_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_name_2 = 'Saw'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_1)
        books_collector.add_book_in_favorites(book_name_2)
        books_collector.delete_book_from_favorites(book_name_2)

        assert books_collector.favorites == [book_name_1]

    # 14 Positive test of method "get_list_of_favorites_books"
    def test_get_list_of_favorites_books_correct(self):
        books_collector = BooksCollector()
        book_name_1 = 'Lord of the Rings'
        book_name_2 = 'Saw'

        books_collector.add_new_book(book_name_1)
        books_collector.add_new_book(book_name_2)
        books_collector.add_book_in_favorites(book_name_1)
        books_collector.add_book_in_favorites(book_name_2)

        assert books_collector.get_list_of_favorites_books() == [book_name_1, book_name_2]