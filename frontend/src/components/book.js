import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * The Book component renders a book page based on the current page number.
 * It fetches the current page data from the server and updates the state
 * with the fetched data. It also handles loading state and logs errors if
 * the fetch operation fails.
 * The component renders a book cover with a start button if the current page
 * is 0. Otherwise, it renders a book page with page content, options, and a
 * page number.
 * The component also handles user input by calling the handleStart, handleRestart,
 * handleOption1, and handleOption2 functions when the corresponding buttons
 * are clicked.
 */
const Book = () => {
  const [currentPage, setCurrentPage] = useState(0);
  const [pageContent, setPageContent] = useState({});
  const [bookTitle, setBookTitle] = useState({title:""});
  const [option, setOption] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  
useEffect(() => {
/**
 * Fetches the current page data from the server.
 * If the current page is 0, it retrieves the title object of the book.
 * Otherwise, it retrieves the content object of the page based on the selected option.
 * Updates the corresponding state variables with the fetched data.
 * Handles loading state and logs errors if the fetch operation fails.
 */
    const fetchPage = async () => {
      try {
        if (currentPage === 0) {
          setIsLoading(true);
  
          const title_response = await axios.get(`http://127.0.0.1:5000/api/title`);
          const titleData = title_response.data;
          setBookTitle(titleData);
          
          setIsLoading(false);
        }
        else {
          setIsLoading(true);
          
          const page_response = await axios.get(
            `http://127.0.0.1:5000/api/page/${option}`
          );
          const pageData = JSON.parse(JSON.stringify(page_response.data));
          setPageContent(pageData);
          setIsLoading(false);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
        setIsLoading(false);
      }
    };
  
    fetchPage();
  }, [currentPage, option]);
  
  /**
   * Plays the audio given by the url
   * @param {string} url - the url of the audio
   */
  const playAudio = (url) => {
    const audio = new Audio(url); // Create  audio object with  URL
    audio.play().catch((error) => console.error("Error playing audio:", error));
  };

  /**
   * Resets the story to the beginning
   */
  const handleRestart = () => {
    setOption(0);
    setCurrentPage(0);
  };


  /**
   * Starts the story by setting the page to 1
   */
  const handleStart = () => {
    setOption(0);
    setCurrentPage((prevPage) => prevPage + 1);
  };

/**
 * Updates the state to reflect the user's choice of Option 1
 * and advances the story to the next page.
 */
  const handleOption1 = () => {
    setOption(1);
    setCurrentPage((prevPage) => prevPage + 1);
  };


/**
 * Updates the state to reflect the user's choice of Option 2
 * and advances the story to the next page.
 */
  const handleOption2 = () => {    
    setOption(2);
    setCurrentPage((prevPage) => prevPage + 1);
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }
  else if (currentPage === 0) {
    return (
    <div>
      <div className="book-cover">
        <h1 className="book-title">{bookTitle.title}</h1>
        <img src={bookTitle.image_url} alt="Book Cover" />
        <div className="page-options">
          <button className="start-button" onClick={handleStart}>
            Start
          </button>
        </div>
      </div>
    </div>

  );
  }
  else if (pageContent.status === "Complete") {
    return (
      <div className="book-page">
      <div className="page-content">
        <p className="page-text">{pageContent.part}</p>
      </div>
      <div className="page-options">
        <button className="option-button" onClick={handleRestart}>Read another book</button>
      </div>
      <div className="page-number">{currentPage}</div>
    </div>
    );
  }
  else{
    return (
      <div className="book-page">
        <button 
          className="audio-button" 
          onClick={() => playAudio(pageContent.textURL)}>
            <span>🔊</span>
        </button>
        <div className="page-content">
          <p className="page-text">{pageContent.part}</p>
        </div>
        <div className="page-options">
          <button className="option-button" onClick={handleOption1}>{pageContent.option1}</button>
          <button className="option-button" onClick={handleOption2}>{pageContent.option2}</button>
        </div>
        <div className="page-number">{currentPage}</div>
      </div>
    );
  }
};

export default Book;
