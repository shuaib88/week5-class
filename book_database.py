import csv

class Book:
<<<<<<< HEAD
	def search(self, searchTerm):
		pass

def read_book_data():
	with open("books.csv", "r", encoding="utf-8") as csvFile:
		bookReader = csv.reader(csvFile, delimiter=",")
		
		bookList = []

		for row in bookReader:
			book = Book()
			book.rank = row[1]
			book.name = row[1]
			book.author = row[2]
			book.publisher = row[3]
			bookList.append(book)

	return bookList


bestBooks = read_book_data()

print(bestBooks[0].name)
=======

  def search(term):
    books = Book.load_books_from_csv()

    for book in books:
      if term.lower() in book.title.lower():
        return book

    return None

  def load_books_from_csv():
    all_books = []
    Book.publishers = []

    # Read the list of books from disk
    with open("books.csv") as file:
      reader = csv.reader(file)
      for row in reader:
        if row:
          # Create a new Book instance
          # and add it to our bookshelf
          new_book = Book()
          new_book.title = row[1]
          new_book.author = row[2]
          new_book.publisher = row[3]
          all_books.append(new_book)

          # Update our master list of publishers
          publishers_for_this_book = new_book.publisher.split('/')
          for publisher in publishers_for_this_book:
            publisher = publisher.strip('.')  # remove any trailing period
            if publisher not in Book.publishers:
              Book.publishers.append(publisher)

    return all_books
>>>>>>> FETCH_HEAD
