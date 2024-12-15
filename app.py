import streamlit as st
from Data_Scraping import scrape_article
from Entity_Extraction import extract_entities
from Sentiment_Analysis import analyze_sentiment
from Data_Store import store_data_mongo

# Streamlit UI
st.title("News Article Analyzer")

# Input field for the URL
url = st.text_input("Enter the URL of the news article:")

if url:
    # Step 1: Scrape the article content
    article_text = scrape_article(url)
    
    # Step 2: Extract entities
    entities = extract_entities(article_text)
    
    # Step 3: Analyze sentiment
    sentiment = analyze_sentiment(article_text)
    
    # Display results
    st.subheader("Article Content")
    st.write(article_text)
    
    st.subheader("Extracted Entities")
    st.write(f"Persons: {entities['PERSON']}")
    st.write(f"Organizations: {entities['ORG']}")
    
    st.subheader("Sentiment")
    st.write(f"Sentiment: {sentiment}")
    
    # Step 4: Store data in MongoDB
    store_data_mongo(url, article_text, entities, sentiment)
    
    st.success("Data has been stored successfully in MongoDB!")
