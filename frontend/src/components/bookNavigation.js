import React, { useState, useEffect } from 'react';

const BookNavigation = () => {
    const [currentPage, setCurrentPage] = useState(0);  
    const [pageCount, setPageCount] = useState(0);

    useEffect(() => {
        const fetchPageCount = async () => {
            try {            
                
                setPageCount(response.data);
            } catch (error) {                
                console.error('Error fetching page count:', error);
            }
        };    
        fetchPageCount();
    }, []);

    const handleNextPage = () => {
        setCurrentPage((prevPage) => prevPage + 1);
    };

    const handlePreviousPage = () => {
        setCurrentPage((prevPage) => Math.max(prevPage - 1, 0)); // Prevent going below 0
    };

    return (
        <div>
            <button onClick={handlePreviousPage}>Previous</button>
            <button onClick={handleNextPage}>Next</button>
        </div>
    );
};

export default BookNavigation;