# use postman or anything similar to that for testing below APIs

GET all books:
http://127.0.0.1:5000/books

GET a specific book:
http://127.0.0.1:5000/books/1

POST (create) a book:
Content-Type: application/json" -d '{"title": "New Book", "author": "New Author"}' http://127.0.0.1:5000/books

PUT (update) a book:
"Content-Type: application/json" -d '{"title": "Updated Book", "author": "Updated Author"}' http://127.0.0.1:5000/books/1

DELETE a book:
DELETE http://127.0.0.1:5000/books/1