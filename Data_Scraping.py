import requests
from bs4 import BeautifulSoup

# Function to scrape the HTML content from a URL
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        article = soup.find('article')  # Change this based on the website structure
        if article:
            return article.get_text()
        else:
            return "Article content not found!"
    except Exception as e:
        return f"Error: {e}"
