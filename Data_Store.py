from pymongo import MongoClient
from urllib.parse import quote_plus

# URL encode the password
password = quote_plus("Ajay@123")

# MongoDB URI with the encoded password
uri = f"mongodb+srv://Escobar:{password}@news-sentiment-analysis.ai85x.mongodb.net/"

# Connect to MongoDB
client = MongoClient(uri)

db = client['news_articles_db']  # Database
collection = db['articles']  # Collection where articles will be stored

# Function to store data in MongoDB
def store_data_mongo(url, article, entities, sentiment):
    article_data = {
        "url": url,
        "article": article,
        "entities": entities,
        "sentiment": sentiment
    }
    
    # Insert data into MongoDB
    collection.insert_one(article_data)
    print("Data stored successfully!")





