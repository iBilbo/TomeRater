import operator

class User(object):
    """User has a name, an email, and a dictionary of books with optional ratings for each book."""

    def __init__(self, name, email):
        """Constructor to set name, email and an empty dictionary of books"""
        if email.find("@") != -1 or email.find(".com") != -1 and email.find(".org") != -1 and email.find(".edu") != -1:

            self.name = name
            self.email = email
            self.books = {}
        else:
            print("The email {email} is not correct. Please enter a valid email address".format(email=email))

    def __repr__(self):
        """Returns a message with name, email, and number of books read by the user"""
        return "User: " + str(self.name) + ", email: " + str(self.email) + ", books read: " + str(self.books)

    def __eq__(self, other_user):
        """Compare two User objects by name and email"""
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def get_email(self):
        """Returns the user´s email address"""
        return self.email

    def change_email(self, address):
        """Updates a user´s email address by passing the new address as argument and prints an info message"""
        if address.find("@") != -1 or address.find(".com") != -1 and address.find(".org") != -1 and address.find(".edu") != -1:
            self.email = address
            print("The email has been updated to " + str(self.email))
        else:
            print("The email {email} is not correct. Please enter a valid email address".format(email=address))

    def read_book(self, book, rating=None):
        """Adds a book to the books dictionary with an optional rating."""
        self.books[book] = rating

    def get_average_rating(self):
        """Returns the average rating for all books with a rating."""
        total = 0
        counter = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating:
                    total += rating
                    counter += 1
                else:
                    continue
        if counter > 0:
            return total / counter
        else:
            print("There are no books with ratings for {user}".format(user=self.name))

    def get_books_read(self):
        """Returns the books read by a user"""
        return self.books

    def get_n_books_read(self):
        """Method used for getting the list of most prolific readers"""
        return len(self.books)

class Book(object):
    """Book has a title, a ISBN and a list of optional ratings. Books will have two subclasses Fiction (novel) and
    Non Fiction. Attribute price added for the Get Creative! section"""

    def __init__(self, title, isbn, price):
        """Constructor to set the title and the ISBN of a book and also an empty list for ratings. """
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __hash__(self):
        """Creates a hash method for the Book object. This is used to have the Book instances used as keys in the
        books dictionary in the User object."""
        return hash((self.title, self.isbn, self.price))

    def __eq__(self, other_book):
        """Compare two Book objects by title and ISBN"""
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def __repr__(self):
        """Returns a message with name, email, and number of books read by the user"""
        return "{title} with ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def get_title(self):
        """Returns the title of a Book instance"""
        return self.title

    def get_isbn(self):
        """Returns the ISBN of a Book instance"""
        return self.isbn

    def set_isbn(self, new_isbn):
        """Set a new ISBN to a Book instance"""
        self.isbn = new_isbn
        print("The ISBN has been updated to " + str(self.isbn))

    def add_rating(self, rating):
        """Add a valid rating to a Book instance"""
        if rating >= 0 and rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating!!!")

    def get_average_rating(self):
        """Returns tha average rating of a Book instance"""
        total_rating = 0
        for i in range(len(self.ratings)):
            total_rating += self.ratings[i]
        return total_rating / len(self.ratings)

    #Get creative! section method
    def get_price(self):
        return self.price


class Fiction(Book):
    """Fiction is a subclass of Book with author as extra attribute"""

    def __init__(self, title, author, isbn, price):
        """Constructor that inherits title and ISBN from Book superclass and set the author"""
        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
        """Return a message with title and author"""
        return str(self.title) + " by " + str(self.author)

    def get_author(self):
        """Returns the author of a Fiction instance"""
        return self.author

class Non_Fiction(Book):
    """Non Fiction is a subclass of Book with subject and level as extra attributes"""

    def __init__(self, title, subject, level, isbn, price):
        """Constructor that inherits title and ISBN from Book superclass and set the subject and the level"""
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):
        """Returns a message with title, level and subject of a Non Fiction instance"""
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        """Returns the subject of a Non Fiction instance"""
        return self.subject

    def get_level(self):
        """Returns the level of a Non Fiction instance"""
        return self.level

class TomeRater:
    """Interacts between Users and Book instances"""

    def __init__(self):
        """Set two empty dictionaries, one for users and one for books"""
        self.users = {}
        self.books = {}

    def __repr__(self):
        """Returns number of users, number of books, highest rated book, most read book and the most positive user"""
        n_users = len(self.users)
        n_books = len(self.books)
        highest_rated = self.highest_rated_book()
        most_read = self.most_read_book()
        most_positive = self.most_positive_user()
        return "This TomeRater has {n_users} users and {n_books} books.\n The highest rated book is {highest} and the most read is {most_read}.\n And the user giving the most positive reviews is: {positive}".format(n_users=n_users, n_books=n_books, highest=highest_rated, most_read=most_read, positive=most_positive)

    def __eq__(self, other):
        """Compare between two instances of TomeRater by comparing books and users dictionaries"""
        if self.books == other.books and self.users == other.users:
            print("These two TomeRater instances are equal!")
            return True
        else:
            print("These two TomeRater instances are NOT equal!")
            return False

    def create_book(self, title, isbn, price):
        """Returns a new instance of Book"""
        isbns=[]
        for book in self.books.keys():
            isbns.append(book.get_isbn())

        if isbn in isbns:
            print("The ISBN {isbn} is already assigned to a book. Please use a unique ISBN.".format(isbn=isbn))
        else:
            new_book = Book(title, isbn, price)
            return new_book

    def create_novel(self, title, author, isbn, price):
        """Returns a new instance of Fiction subclass"""
        isbns = []
        for book in self.books:
            isbns.append(book.get_isbn())

        if isbn in isbns:
            print("The ISBN {isbn} is already assigned to a book. Please use a unique ISBN.".format(isbn=isbn))
        else:
            new_novel = Fiction(title, author, isbn, price)
            return new_novel

    def create_non_fiction(self, title, subject, level, isbn, price):
        """Returns a new instance of Non Fiction subclass"""
        isbns = []
        for book in self.books:
            isbns.append(book.get_isbn())

        if isbn in isbns:
            print("The ISBN {isbn} is already assigned to a book. Please use a unique ISBN.".format(isbn=isbn))
        else:
            new_non_fiction = Non_Fiction(title, subject, level, isbn, price)
            return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        """Adds a book to a user"""
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)

            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}".format(email=email))

    def add_user(self, name, email, user_books=None):
        """Creates a User instance and uses the add_book_to_user method to add the book list of the user"""
        user = self.users.get(email)
        if user:
            print("The user with email {email} already exists. Please select a different email address". format(email=email))
        else:
            new_user = User(name, email)
            self.users[email] = new_user

            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        """Prints the keys of the books dictionary"""
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """prints the keys of the users dictionary"""
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        """Returns the most read book"""
        max_read_book = 0
        read_book = ""
        for book, reads in self.books.items():
            if reads > max_read_book:
                max_read_book = reads
                read_book = book
            else:
                continue
        return read_book

    def highest_rated_book(self):
        """Returns the book with a highest rating"""
        rated_book = ""
        max_rating = 0

        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                rated_book = book
                max_rating = rating
            else:
                continue

        return rated_book

    def most_positive_user(self):
        """Returns the user that provides the highest average rating"""
        rated_user = ""
        max_rating = 0

        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > max_rating:
                rated_user = user
                max_rating = rating
            else:
                continue

        return rated_user

    #Get Creative! section methods:
    def get_n_most_read_books(self, n):
        """Returns the n most read books"""
        sorted_books = sorted(self.books, key=self.books.get, reverse=True)
        return sorted_books[:n]

    def get_n_most_prolific_readers(self, n):
        """Returns the n users with more read books"""
        readers = []
        sorted_readers = []

        for reader in self.users.values():
            books_readed = reader.get_n_books_read()
            readers.append((reader, books_readed))

        for k in sorted(readers, key=lambda reader: reader[1], reverse=True):
            sorted_readers.append(k[0])
        return sorted_readers[:n]


    def get_n_most_expensive_books(self, n):
        """Returns a list with the n most expensive books. Imported operator module to use itemgetter()"""
        books_price = {book: book.get_price() for book in self.books.keys()}
        sorted_prices = sorted(books_price.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_prices[:n]

    def get_worth_of_user(self, user_email):
        """Returns the sum of the costs of all of the books read by a user"""
        sum_price_books = 0
        user = self.users.get(user_email)
        books_read_by_user = user.get_books_read()

        for book in books_read_by_user.keys():
            sum_price_books += book.get_price()
        return "The total cost of the books read by {name}({email}) is ${price}.".format(name=user.name, email=user_email, price=sum_price_books)
