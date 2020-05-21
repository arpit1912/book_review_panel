import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:arpit@localhost/project1')
db = scoped_session(sessionmaker(bind=engine))
#isbn,title,author,year
def main():
	f = open("books.csv")
	reader = csv.reader(f)
	for isbn, title, author, year in reader:
		print(f"Added book with isbn number {isbn} with title {title} by {author}")
		db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:is, :ti,:au, :ye)",{"is":isbn, "ti":title, "au":author, "ye":year})
	db.commit()

if __name__ == "__main__":
	main()

