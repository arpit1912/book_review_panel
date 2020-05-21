# book_review_panel

In this Application Postgres has been used as a database so make you change the SQLAlchemy url accordingly and also create the specific tables needed for this Application,make sure u change the API key for Google Read too as this application make API calls to fetch reviews.

This website is a book reviewing/viewing panel for 5000 books.The user has to create a account for login in into the appication. The user then login using his user_id and password to go the search page where he/she can actually look back for his book.
![Login Page](https://github.com/arpit1912/book_review_panel/blob/master/login_page.png)

On the search page Users can type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, the website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, the  search page will find matches for those as well!
![Search Page](https://github.com/arpit1912/book_review_panel/blob/master/search_page.png)

Here is the look of the results for a query
![Search Results](https://github.com/arpit1912/book_review_panel/blob/master/results.png)

On selecting a book the user will be taken to the Review panel where he/she can see the details of the books as well as the review of the book on the google read. Here the server is fetching the review using an API call so make sure to fill the api key corresponding to your id before running this application.
![Review form](https://github.com/arpit1912/book_review_panel/blob/master/review_panel.png)

Each User can submit only one review for a given book, if visited again by the same user the page will show his earlier review as shown below.
![Review Again](https://github.com/arpit1912/book_review_panel/blob/master/after_review.png)

