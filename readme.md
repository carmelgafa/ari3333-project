# Interactive Book - Assignment for ARI3333

## 2025  

---

This repository contains the source code, documentation, and instructions for the Interactive Book assignment for ARI3333.

## Overview  

The **Interactive Book** system is a single-page application designed to deliver an engaging storytelling experience. It combines cutting-edge technologies like React for the frontend, Flask for the backend, and services like OpenAI and Azure Cognitive Services for dynamic content and audio generation. The system highlights the beauty of modern web architecture by integrating multiple services seamlessly to create an immersive interactive narrative.

### Features

- **Interactive Storytelling:** The system provides an engaging narrative with user-driven choices.
- **Dynamic Content:** Stories are generated dynamically using OpenAI's API for text generation.
- **Immersive Audio:** Audio narration is seamlessly integrated using Azure Cognitive Services.
- **Modern Web Architecture:** The system is designed with modularity in mind, using a React frontend and Flask backend for a clean separation of concerns.


## System Architecture

The system is composed of two primary components:

1. Frontend
    - Developed using React.
    - Handles user interaction and dynamically displays generated content.
2. Backend
    - Built using Flask.
    - Communicates with OpenAI for text generation and Azure Cognitive Services for text-to-speech functionality.
    - File Server Serves audio files generated by Azure Cognitive Services.

## Project Directory Structure

Below is a high-level overview of the project directory structure:

```bash
├── backend/               # Flask application folder  
│   ├── app.py             # Main Flask application file  
│   ├── requirements.txt   # Python dependencies  
│   ├── ...                # Other backend scripts and files
├── frontend/              # React application folder  
│   ├── src/               # Source files for the React app  
│   ├── public/            # HTML file launching the frontend app
│   ├── package.json       # npm dependencies  
│   ├── ...                # Other frontend files and utilities  
├── doc/                   # Report for this project
├── README.md              # Project documentation  
```

### Source Code  

The source code is organized into the following folders:  

- `frontend`: Contains the React application for the user interface.  
- `backend`: Contains the Python-based Flask server that interacts with OpenAI's APIs for text generation and Azure Cognitive Services for text-to-speech functionality.  

## Prerequisites  

Before running the application, ensure you have the following dependencies installed on your system:  

- **Node.js**: Version `16.20.2` or higher.  
- **Python**: Version `3.12.5` or higher.  

Additional dependencies (e.g., Python libraries or npm packages) can be installed using the respective package managers (`pip` and `npm`).

## Application Execution  

To run the application, follow these steps:  

1. **Start the Web Server**  
   Navigate to the folder where the generated sound files are stored and run a web server to serve these files. Use the following command:  

```bash
    npx http-server  
```

2. **Run the Flask Backend**
Open a terminal window, navigate to the backend folder, and run the Flask application.
Execute the following command:

```bash
python app.py  
```

3. **Run the Frontend (React Application)**
Open a third terminal, navigate to the frontend folder, and start the React frontend application:

```bash
npm start  
```

### Additional Notes

- Ensure that the backend Flask server is running before launching the React frontend application to avoid connection errors.
- The sound files generated by Azure Cognitive Services should be accessible through the web server started in Step 1.
- For any configuration or runtime errors, refer to the detailed logs provided by Flask and React during execution.



---

This text was polished from a very crude version by openai
