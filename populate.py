from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 20)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 16)
#novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 22)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 32)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010,15)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 20)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Test Duplicate user:
#Tome_Rater.add_user("David Yates", "david@computation.org")


#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Test duplicate ISBN:
#novel4 = Tome_Rater.create_novel("Cien Noches de Soledad", "Gabriel Garcia Marquez", 10001000)

#Uncomment these to test your functions:
print("THE CATALOG: ")
Tome_Rater.print_catalog()
print("USER LIST: ")
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print("Most 3 read books: ")
print(Tome_Rater.get_n_most_read_books(3))
print("Most prolific readers: ")
print(Tome_Rater.get_n_most_prolific_readers(3))
print("Most expensive books: ")
print(Tome_Rater.get_n_most_expensive_books(4))
print("Worth of user: ")
print(Tome_Rater.get_worth_of_user("alan@turing.com"))








# Primary Tests
# bilbo =  User("Alvaro", "abt@gmail.com")
# print(bilbo)
# print(bilbo.get_email())
# print(bilbo.change_email("newabt@gmail.com"))
# print(bilbo.get_email())
# alice = Book("Alice in Wonderland", 12345)
# print(alice)
# print(alice.get_title())
# print(alice.get_isbn())
# print(alice.set_isbn(6789))
# alice.add_rating(8)
# alice.add_rating(4)
# alice2 = Fiction("Alice in Wonderland", "Lewis Carroll", 6789)
# print(alice2)
# print(alice == alice2)
# print(alice2.get_author())
# society = Non_Fiction("Society of Mind", "Artificial Intelligence", "beginner", 112233)
# print(society.get_level())
# print(society)
# tome_rater = TomeRater()
