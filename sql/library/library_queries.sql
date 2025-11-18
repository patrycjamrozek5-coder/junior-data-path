-- SQL Queries for filtering and joining data from LibraryTX database

USE LibraryTX;

-- Filters all books published after 2005
SELECT title, author, year_published FROM Books WHERE year_published > 2005; 

-- Filters all users from Houston
SELECT * FROM Users WHERE city = 'Houston';

-- List all book loans with user name and book title
SELECT title, name, rental_date, return_date
FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
JOIN Books ON Rentals.book_id = Books.book_id;

-- Count number of users who borrowed books
SELECT COUNT(DISTINCT user_id)
FROM Rentals
WHERE rental_date is NOT NULL;

-- List users and their borrowed books
SELECT Rentals.user_id, name, title
FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
JOIN Books ON Rentals.book_id = Books.book_id;

-- Count how many times each book was borrowed
SELECT title, 
COUNT(*)AS 'Number of loans' FROM Rentals 
JOIN Books ON Rentals.book_id = Books.book_id 
GROUP BY title;

-- List users who have never borrowed anything
SELECT * FROM Users 
LEFT JOIN Rentals ON Users.user_id = Rentals.user_id
WHERE Rentals.rental_id IS NULL;
