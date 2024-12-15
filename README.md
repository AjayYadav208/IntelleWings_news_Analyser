# IntelleWing News Sentiment Analysis 🚀

Welcome to the **IntelleWing News Sentiment Analysis**! This project scrapes news articles, extracts entities (persons and organizations), and performs sentiment analysis on the articles.

---

## 📝 **Objective**
The objective of this project is to demonstrate the ability to:
1. Scrape data from news articles using URLs 🌐.
2. Extract entities (persons and organizations) mentioned in the articles 🏢👤.
3. Classify the sentiment of the articles (positive, negative, or neutral) 📊.
4. Store the data in MongoDB 🗄️.
5. Deploy the entire project using Docker 🐳.

---

## 🚀 **Getting Started**

### Prerequisites

1. **Docker**: Make sure Docker Desktop is installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).
2. **Python**: Python 3.x should be installed. You can download it from [here](https://www.python.org/downloads/).

---

### 🛠️ **Installation**

1. Clone this repository or download the project folder to your local machine.

2. Install dependencies:
   - If you're running locally:
     ```bash
     pip install -r requirements.txt
     ```
   
3. Build and run the Docker container:
   - **Build the Docker image**:
     ```bash
     docker build -t my-data-science-app .
     ```

   - **Run the Docker container**:
     ```bash
     docker run -p 8501:8501 my-data-science-app
     ```

   Your application will be available at [http://localhost:8501](http://localhost:8501).

---

## 🧠 **Project Structure**

```
/my_project
  ├── app.py               # Main Streamlit application
  ├── requirements.txt     # Python dependencies
  ├── Dockerfile           # Docker configuration file
  ├── Docker-compose.yml   # (Optional) Docker Compose configuration
  └── README.md            # Project documentation (you are here!)
```

---

## 🏗️ **How It Works**

### 1. **Data Scraping** 🌐
- A Python script fetches HTML content from news article URLs.
- The content is then processed to extract useful information.

### 2. **Entity Extraction** 🔍
- Named Entity Recognition (NER) identifies persons and organizations mentioned in the articles using **spaCy**.

### 3. **Sentiment Analysis** 😄😡😐
- **TextBlob** or any pretrained sentiment model is used to classify the sentiment as positive, negative, or neutral.

### 4. **Data Storage** 🗄️
- The results are stored in **MongoDB**.

---

## 💡 **Usage Example**

1. Input a news article URL.
2. The system will:
   - Scrape the article content.
   - Extract and display the names of persons and organizations.
   - Analyze and display the sentiment of the article.

---

## 🚢 **Deployment on Docker**

1. **Build Docker Image**:
   ```bash
   docker build -t my-data-science-app .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 8501:8501 my-data-science-app
   ```

---

## 🧑‍💻 **Contributing**

Feel free to fork the repository and create pull requests! Contributions are always welcome 😊.

---

## 📜 **License**

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---

## 🎉 **Acknowledgements**

- **Streamlit**: For easy deployment of web applications.
- **spaCy**: For Named Entity Recognition.
- **TextBlob**: For sentiment analysis.
- **MongoDB**: For data storage.

---

Thank you for checking out the project! 🎉
```

---

### **Explanation of Sections**:
1. **Objective**: Describes the purpose of the project.
2. **Getting Started**: Guides the user through prerequisites and installation steps.
3. **Project Structure**: Lists the files and directories in the project.
4. **How It Works**: Explains the core functionality of the application.
5. **Usage Example**: Provides a simple overview of how the app works.
6. **Deployment on Docker**: Explains the Docker deployment process.
7. **Contributing**: Encourages others to contribute to the project.
8. **License**: Specifies the project's license.
9. **Acknowledgements**: Credits external libraries and tools used in the project.

---