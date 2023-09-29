# FILEPATH: streamlit_app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_reviews(url):
    # Send a GET request to the app URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div that contains the reviews
    reviews_div = soup.find('div', {'class': 'W4P4ne'})

    # Extract the reviews from the div
    reviews = []
    for review_div in reviews_div.find_all('div', {'class': 'd15Mdf bAhLNe'}):
        review = {}
        review['author'] = review_div.find('span', {'class': 'X43Kjb'}).text
        review['date'] = review_div.find('span', {'class': 'p2TkOb'}).text
        review['rating'] = int(review_div.find('div', {'class': 'pf5lIe'}).find('div')['aria-label'].split()[1])
        review['comment'] = review_div.find('div', {'class': 'UD7Dzf'}).text
        reviews.append(review)

    return reviews

# Set up the Streamlit app
st.set_page_config(page_title="Google Play Store Review Extractor", page_icon=":memo:", layout="wide")
st.title('Google Play Store Review Extractor')

# Get the app URL from the user
url = st.text_input('Enter the URL of the app in the Google Play Store:', help="Example: https://play.google.com/store/apps/details?id=com.google.android.apps.maps")

# If the user has entered a URL, extract the reviews and display them
if url:
    st.write(f'Extracting reviews from {url}...')
    reviews = get_reviews(url)
    st.write(f'Found {len(reviews)} reviews:')
    for review in reviews:
        st.write(f"Author: {review['author']}")
        st.write(f"Date: {review['date']}")
        st.write(f"Rating: {review['rating']}")
        st.write(f"Comment: {review['comment']}")
        st.write('---')
else:
    st.write("Please enter the URL of the app in the Google Play Store above.")
