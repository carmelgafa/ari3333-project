import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Book = () => {
  const [currentPage, setCurrentPage] = useState(0);
  const [pageContent, setPageContent] = useState("");
  const [endPage, setEndPage] = useState(false);

  useEffect(() => 
  {
    const fetchPage = async () =>
    {
      try
      {
        const response = await axios.get(`http://127.0.0.1:5000/api/page/${currentPage}`);
        const pageContent = response.data.content;
        console.log(pageContent);
        setPageContent(pageContent);
        if (pageContent === "The End")
        {
          setEndPage(true);
        }
        else if (endPage) {
          setEndPage(false);
        }
      } 
      catch (error) 
      {
        console.error("Error fetching page:", error);
        setPageContent("Error loading page"); // Display error message if fetch fails
      }
    };
    fetchPage();
  }, [currentPage]); // Trigger this effect every time currentPage changes

  const handleNextPage = () => {
    setCurrentPage((prevPage) => prevPage + 1);
  };

  const handlePreviousPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 0)); // Prevent going below 0
  };

  return (
    <div className="book-container">
      
      <div className="pages-container">
        <div className="page">
          <h3>Page {currentPage + 1}</h3>
          <p>{pageContent}</p>
        </div>
        <div className="page">
          <h3>Page {currentPage + 1}</h3>
      </div>
    </div>

      <div className="navigation">
        <button onClick={handlePreviousPage} disabled={currentPage === 0}>
          Previous
        </button>
        
        {endPage ? (
          <p></p>
        ) : (
          <button onClick={handleNextPage}>
            Next
          </button>
        )}
      </div>
    </div>
  );
};

export default Book;
