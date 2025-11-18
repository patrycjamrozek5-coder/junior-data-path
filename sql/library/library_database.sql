-- Mini Library Database
-- Created for SQL practice
-- Contains: Books, Users, Rentals
-- Author: Patrycja Mrożek
-- Date: 2025-11-18

CREATE DATABASE LibraryTX;   -- Create new database for the project
USE LibraryTX;

CREATE TABLE Books (         -- Books table: stores information about books in the library
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author VARCHAR(100),
    year_published INT,
    rating DECIMAL(3,2)
);

CREATE TABLE Users (         -- Users table: stores information about library users
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE Rentals (        -- Rentals table: records which user rented which book and when
    rental_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    rental_date DATE,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

INSERT INTO Books (title, author, year_published, rating)  -- Insert sample book data
	VALUES 
		('Harry Potter and the Deathly Hallows', 'J.K. Rowling', 2007, 4.62),
        ('The Book Thief', 'Markus Zusak', 2005, 4.39),
        ('The Hunger Games', 'Suzanne Collins', 2008, 4.35),
        ('Pride and Prejudice', 'Jane Austen', 1813, 4.29),
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 4.26),
        ('The Lightning Thief', 'Rick Riordan', 2005, 4.25),
        ('1984', 'George Orwell', 1949, 4.20),
        ('The Fault in Our Stars', 'John Green', 2012, 4.12)
;

INSERT INTO Users (name, city)     -- Insert sample user data
	VALUES
		('Caroline Fleming', 'San Antonio'), 
        ('Aiko Tanaka', 'Houston'),
        ('Sofia Dimitrova', 'San Antonio'),
        ('Jonas Lindberg', 'Austin'),
        ('Hannah McConnell', 'Houston'),
        ('Liam Carter', 'Austin')
;

INSERT INTO rentals (user_id, book_id, rental_date, return_date)   -- Insert sample rentals data
	VALUES
		(1, 1, '2025-08-25', '2025-09-01'),
        (2, 1, '2024-01-10', '2024-01-17'),
		(2, 3, '2024-01-20', '2024-01-28'),
		(2, 4, '2024-02-01', NULL),
		(2, 2, '2024-02-10', '2024-02-20'),
		(2, 5, '2024-03-01', NULL),
		(3, 6, '2024-05-14', '2024-05-28'),
		(3, 8, '2024-06-02', NULL),
		(4, 1, '2024-03-10', '2024-03-20'),
		(4, 7, '2024-04-01', NULL),
		(5, 3, '2024-02-12', '2024-02-19')
;

