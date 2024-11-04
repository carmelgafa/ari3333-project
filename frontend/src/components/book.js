// src/components/Book.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Book = () => {
  const [pages, setPages] = useState([]);
  const [currentPage, setCurrentPage] = useState(0);

  useEffect(() => {
    const fetchPages = async () => {
      const fetchedPages = [];
      for (let i = 0; i < 4; i++) { // Adjust the page count as needed
        try {
          const response = await axios.get(`http://127.0.0.1:5000/api/page/${i}`);
          fetchedPages.push(response.data.content);
        } catch (error) {
          fetchedPages.push("Error loading page");
        }
      }
      setPages(fetchedPages);
    };

    fetchPages();
  }, []);

  const handleNext = () => {
    if (currentPage < pages.length - 1) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const handlePrevious = () => {
    if (currentPage > 0) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  return (
    <div className="book-container">
      <div className="page">
        <h3>Page {currentPage + 1}</h3>
        <p>{pages[currentPage]}</p>
      </div>

      <div className="navigation">
        <button onClick={handlePrevious} disabled={currentPage === 0}>
          Previous
        </button>
        <button onClick={handleNext} disabled={currentPage >= pages.length - 1}>
          Next
        </button>
      </div>
    </div>
  );
};

export default Book;
