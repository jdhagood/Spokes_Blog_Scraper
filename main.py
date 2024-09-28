from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Chrome()

import requests
from bs4 import BeautifulSoup

def get_soup(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    else:
        raise f"Failed to retrieve the page at {url}. Status code: {response.status_code}"

def get_blog_URLs():
    """
    Scrapes all dynamically loaded URLs from 'a' elements with a specific class by scrolling down the page.
    
    Parameters:
        url (str): The URL of the webpage to scrape.
        
    Returns:
        list of str: A list of URLs as strings.
    """
    url = "https://www.mitspokes.com/blog"
    # Set up the Selenium WebDriver (using Chrome in this case)
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in your PATH

    # Open the URL in the browser
    driver.get(url)

    # Scroll down the page to load more content dynamically
    SCROLL_PAUSE_TIME = 2  # Adjust this time if needed

    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the new content to load
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate the new scroll height after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Break the loop if the scroll height hasn't changed (no new content)
        if new_height == last_height:
            break
        last_height = new_height

    # Once the page has fully loaded, scrape the URLs
    a_elements = driver.find_elements(By.CLASS_NAME, "O16KGI.pu51Xe.UUSLFD.mqysW5.has-custom-focus.i6wKmL")
    
    # Extract the URLs from the 'href' attributes
    urls = [a.get_attribute('href') for a in a_elements if a.get_attribute('href')]

    # Close the browser session
    driver.quit()

    return urls

def scrape_blog(url):
    soup = get_soup(url)
    if soup:
        blog = {
            "url": url,
            "title": None,
            "by": None,
            "paragraphs": None,
            "image_dir": None
        }
        blog["title"] = soup.find('span', {'class' : 'blog-post-title-font blog-post-title-color'}).text
        return blog
    return None

#print(scrape_blog("https://www.mitspokes.com/post/day-75-the-real-spokes-ogs"))
print(get_blog_URLs())

# soup = get_soup("https://www.mitspokes.com/post/day-75-the-real-spokes-ogs")
# # Extract text from the entire page
# text = soup.get_text()

# # Optionally, clean up and print the text
# cleaned_text = text.strip()
# print(cleaned_text)