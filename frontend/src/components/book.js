import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Book = () => {
  const [currentPage, setCurrentPage] = useState(0);
  const [pageContent, setPageContent] = useState({});
  const [bookTitle, setBookTitle] = useState({title:""});
  const [option, setOption] = useState(0);
  const [image_url, setImage_url] = useState("");
  const [isLoading, setIsLoading] = useState(false);

useEffect(() => {
    const fetchPage = async () => {
      try {
        if (currentPage === 0) {
          setIsLoading(true);
  
          const title_response = await axios.get(`http://127.0.0.1:5000/api/title`);
          const titleData = title_response.data;
          setBookTitle(titleData);
          
          console.log(titleData);

          const image_response = await axios.get(
            `http://127.0.0.1:5000/api/image/${encodeURIComponent(titleData.title)}`
          );
          const imageData = image_response.data;
  
          console.log(imageData);

          const img = new Image();
          img.src = imageData.image_url;
          img.onload = () => {
            setImage_url(imageData.image_url);
            setIsLoading(false);
          };
        }
        else {
          setIsLoading(true);
  
          const page_response = await axios.get(
            `http://127.0.0.1:5000/api/page/${option}`
          );
          const pageData = JSON.parse(page_response.data);
          

          setPageContent(pageData);
          console.log(pageData);
          console.log(pageContent.part);
  

          setIsLoading(false);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
        setIsLoading(false);
      }
    };
  
    fetchPage();
  }, [currentPage]);
  


  const handleRestart = () => {
    setOption(0);
    setCurrentPage(0);
  };


  const handleStart = () => {
    setOption(0);
    setCurrentPage((prevPage) => prevPage + 1);
  };

  const handleOption1 = () => {
    setOption(1);
    setCurrentPage((prevPage) => prevPage + 1);
  };

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
      <div class="book-cover">
        <h1 class="book-title">{bookTitle.title}</h1>
        <img src={image_url} alt="Book Cover" />
        <div className="page-options">
          <button class="start-button" onClick={handleStart}>
            Start
          </button>
        </div>
      </div>
    </div>

  );
  }
  else if (pageContent.status === "Complete") {
    return (
      <div class="book-page">
      <div class="page-content">
        <p class="page-text">{pageContent.part}</p>
      </div>
      <div class="page-options">
        <button class="option-button" onClick={handleRestart}>Read another book</button>
      </div>
      <div class="page-number">{currentPage}</div>
    </div>
    );
  }
  else{
    return (
        <div class="book-page">
          <div class="page-content">
            <p class="page-text">{pageContent.part}</p>
          </div>
          <div class="page-options">
            <button class="option-button" onClick={handleOption1}>{pageContent.option1}</button>
            <button class="option-button" onClick={handleOption2}>{pageContent.option2}</button>
          </div>
          <div class="page-number">{currentPage}</div>
        </div>
    );
  }



  // return (



  //   <div className="book-container">
  //     <h1>{bookTitle.title}</h1>
  //     <div className="page-content">
  //       <h3>Page {currentPage}</h3>
  //       {<p>{pageContent.part}</p> }

  //       {<p>{pageContent.status}</p> }
  //       {<p>Option 1: {pageContent.option1}</p>}
  //       {<p>Option 2: {pageContent.option2}</p>}
  //     </div>

  //     <div className="navigation">
  //       <button onClick={handleOption1} disabled={currentPage === 0}>
  //         Option 1
  //       </button>
        
  //       {!endPage && (
  //         <button onClick={handleOption2}>
  //           Option 2
  //         </button>
  //       )}
  //     </div>
  //   </div>
  // );
};

export default Book;
