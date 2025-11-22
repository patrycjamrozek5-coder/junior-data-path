-- LibraryTX - Updates and Practice Queries
-- Contains examples of UPDATE, DELETE, filtering, JOINs, COUNT, CASE, LEFT JOIN
-- Author: Patrycja Mrożek
-- Date: 2025-11-18

USE LibraryTX;

-- 1. Data updates

-- Update the rating of the book with ID 4
UPDATE Books SET rating = 5.0 WHERE book_id = 4;

-- Delete old rentals (before 2021)
DELETE FROM Rentals WHERE rental_date < '2021-01-01';

-- Insert an extra book for testing
INSERT INTO Books (title, author, year_published, rating)
VALUES ('Lonely Book', 'Unknown Author', 2025, 3.50);

-- 2. Basic filters and MIN / oldest rental

-- Filter the oldest rental date
SELECT MIN(rental_date) AS oldest_rental_date
FROM Rentals;

-- User who borrowed the book earliest
SELECT Users.name, Rentals.rental_date FROM Rentals
JOIN Users ON Users.user_id = Rentals.user_id
WHERE Rentals.rental_date = (
SELECT MIN(Rentals.rental_date) FROM Rentals);


-- Filters - the books with the highest rating
SELECT title, rating FROM Books
WHERE rating > 4.3
ORDER BY rating DESC;

-- Filter all books whose title starts with 'T'
SELECT title, author FROM Books 
WHERE title LIKE "T%";

-- Filter all users whose names contain 'a' or 'A'
SELECT name, city FROM Users 
WHERE name LIKE "%a%";


-- 3. Aggregation: COUNT, GROUP BY

-- Number of rentals made by user with ID = 2
SELECT user_id, COUNT(*) FROM Rentals
WHERE user_id = 2
GROUP BY user_id;

-- Number of times each book was rented
SELECT Books.title, COUNT(*) AS total_rentals FROM Rentals
JOIN Books ON Rentals.book_id = Books.book_id
GROUP BY Books.title;

-- Number of users from Houston
SELECT COUNT(*) AS user_HOUSTON FROM Users
WHERE city = "Houston";

-- Number of books with rating below 4.2
SELECT COUNT(*) FROM Books
WHERE rating < 4.2;

-- Number of borrowed books per city
SELECT Users.city, COUNT(*) AS city_borrowed_books FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
GROUP BY Users.city;

-- How many different books each user has borrowed
SELECT Users.name, COUNT(DISTINCT Rentals.book_id) AS users_amount_books FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
GROUP BY Users.name;


-- 4. Most frequent / most active

-- Filtering- most frequently borrowed book
SELECT Books.title, COUNT(*) AS borrowed_numbers FROM Rentals
JOIN Books ON Books.book_id = Rentals.book_id
GROUP BY Books.title
ORDER BY borrowed_numbers DESC LIMIT 1;

-- Filters - user who borrowed the most books
SELECT Users.name, COUNT(*) AS amount_of_book
FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
GROUP BY Users.name
ORDER BY amount_of_book DESC LIMIT 1;


-- 5. JOIN examples (INNER JOIN)

-- User and book title for each rental
SELECT Books.title, Users.name FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
JOIN Books ON Rentals.book_id = Books.book_id;

-- User, book title and return date
SELECT Users.name, Books.title, Rentals.return_date FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
JOIN Books ON Rentals.book_id = Books.book_id;

-- Total rentals per user
SELECT Users.name, 
    COUNT(Rentals.rental_id) AS total_rentals FROM Rentals
JOIN Users ON Rentals.user_id = Users.user_id
GROUP BY Users.name;


-- 6.JOIN examples (LEFT JOIN)

-- List all users with titles of books they borrowed (NULL if none)
SELECT Users.name, Books.title FROM Users 
LEFT JOIN Rentals ON Users.user_id = Rentals.user_id 
LEFT JOIN Books ON Rentals.book_id = Books.book_id;

-- Same as above, but shows book_id instead of title (useful for technical checks)
SELECT Users.name, Rentals.book_id 
FROM Users
LEFT JOIN Rentals ON Users.user_id = Rentals.user_id
LEFT JOIN Books ON Rentals.book_id = Books.book_id;


-- 7. CASE examples (labeling)

-- Label books by rating
SELECT title, rating, 
CASE 
    WHEN rating > 4.4 THEN "high"
    WHEN rating BETWEEN 4.0 AND 4.4 THEN "medium"
    ELSE "low"
END AS rating_label 
FROM Books;

-- Label users by activity based on number of rentals
SELECT Users.name,
    COUNT(Rentals.rental_id) AS total_rentals,
CASE 
    WHEN COUNT(Rentals.rental_id) >= 3 THEN "active"
    WHEN COUNT(Rentals.rental_id) BETWEEN 1 AND 2 THEN "regular"
    ELSE "inactive"
END AS activity_level
FROM Users
LEFT JOIN Rentals ON Rentals.user_id = Users.user_id
GROUP BY Users.user_id, Users.name;


-- 8. LEFT JOIN vs INNER JOIN

-- INNER JOIN: only rentals that exist (no NULLs)
SELECT Books.title, Books.author, Rentals.rental_date FROM Rentals
JOIN Books ON Rentals.book_id = Books.book_id;

-- LEFT JOIN: show all books, even if they were never rented
SELECT Books.title, Books.author, Rentals.rental_date FROM Books
LEFT JOIN Rentals ON Books.book_id = Rentals.book_id;





