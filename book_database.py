import csv

class Book:
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