from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

#driver = webdriver.Chrome()

import requests
from bs4 import BeautifulSoup

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_blog_URLs():
    """
    Scrapes all dynamically loaded URLs from elements with a specific class 'O16KGI.pu51Xe.UUSLFD.mqysW5.has-custom-focus.i6wKmL' by scrolling down the page.
    
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

#output from get_blog_urls
urls =['https://www.mitspokes.com/post/day-75-the-real-spokes-ogs', 'https://www.mitspokes.com/post/day-74-the-finale', 'https://www.mitspokes.com/post/day-73-28-things-you-have-to-do-before-we-both-die', 'https://www.mitspokes.com/post/day-72-the-promised-lands-portugal-and-sacramento', 'https://www.mitspokes.com/post/day-71-bumming-around-savoring-every-moment', 
 'https://www.mitspokes.com/post/day-70-the-curse-ends', 'https://www.mitspokes.com/post/day-69-lifestyle-whiplash', 'https://www.mitspokes.com/post/day-69-the-first-of-many-lasts', 'https://www.mitspokes.com/post/day-67-one-final-ass-whooping-from-nevada', 'https://www.mitspokes.com/post/day-66-the-oasis-of-nevada', 'https://www.mitspokes.com/post/day-65-me-and-the-flies-against-the-world', 'https://www.mitspokes.com/post/day-64-a-non-biking-day-in-portugal',
   'https://www.mitspokes.com/post/day-63-we-love-stickers', 'https://www.mitspokes.com/post/day-62-senioritis', 'https://www.mitspokes.com/post/day-61-desert-magic', 'https://www.mitspokes.com/post/day-60-a-how-to-guide-for-boring-rides', 'https://www.mitspokes.com/post/day-59-spokes-in-the-narrows', 'https://www.mitspokes.com/post/day-58-angels-landing-and-angel-s-departing', 'https://www.mitspokes.com/post/day-57-diary-of-a-limpy-kid', 
   'https://www.mitspokes.com/post/look-on-the-bryce-side', 'https://www.mitspokes.com/post/day-55-moo-and-hoodoo-and-food', 'https://www.mitspokes.com/post/day-54-cosmic-gratitude', 'https://www.mitspokes.com/post/day-53-we-can-t-read-signs', 'https://www.mitspokes.com/post/day-52-ah-shit-here-we-go-again', 'https://www.mitspokes.com/post/day-51-jackass-joe-s', 'https://www.mitspokes.com/post/day-50-sunsets-and-moonrises', 'https://www.mitspokes.com/post/day-49-delicate-knees-at-delicate-arch', 
   'https://www.mitspokes.com/post/day-48-yay-utah', 'https://www.mitspokes.com/post/what-i-eat-in-a-day', 'https://www.mitspokes.com/post/day-46-call-us-james-cause-it-s-getting-peachy', 'https://www.mitspokes.com/post/day-45-a-goated-day', 'https://www.mitspokes.com/post/day-44-spokes-vs-the-continental-divide', 'https://www.mitspokes.com/post/day-43-i-think-my-life-might-be-better-if-i-lived-in-colorado-mmm', 'https://www.mitspokes.com/post/day-42-reckoning-with-mortality', 'https://www.mitspokes.com/post/day-41-mother-infrastructure',
     'https://www.mitspokes.com/post/denver-rest-day', 'https://www.mitspokes.com/post/day-39-we-re-not-in-kansas-anymore-2', 'https://www.mitspokes.com/post/day-38-it-s-jolene-s-world-and-we-re-all-just-living-in-it', 'https://www.mitspokes.com/post/day-37-junk-in-our-trunk-what-i-packed-for-spokes', 'https://www.mitspokes.com/post/day-36-when-we-re-big-kids', 'https://www.mitspokes.com/post/day-35-i-don-t-think-we-re-in-kansas-anymore', 'https://www.mitspokes.com/post/day-34-which-mit-spokes-member-are-you', 'https://www.mitspokes.com/post/day-33-viva-la-vida', 
     'https://www.mitspokes.com/post/day-32-murica', 'https://www.mitspokes.com/post/day-31-castles-bubble-wands-and-everything-in-between', 'https://www.mitspokes.com/post/day-30-kansas-entrance-exam', 'https://www.mitspokes.com/post/day-29-pick-your-poison', 'https://www.mitspokes.com/post/we-have-the-tour-de-france-at-home-jk', 'https://www.mitspokes.com/post/day-27-41-million-revolutions', 'https://www.mitspokes.com/post/day-26-am-i-dreaming', 'https://www.mitspokes.com/post/day-25-no-more-cars', 'https://www.mitspokes.com/post/day-24-a-rest-day-in-saint-louis',
       'https://www.mitspokes.com/post/day-23', 'https://www.mitspokes.com/post/day-22-it-s-worth-it-the-sunsets', 'https://www.mitspokes.com/post/day-21-a-day-on-4-wheels', 'https://www.mitspokes.com/post/day-20-bushwhacking-and-gravel-riding', 'https://www.mitspokes.com/post/day-19-bowling-green-learning-festival', 'https://www.mitspokes.com/post/day-18-longest-day-of-the-year', 'https://www.mitspokes.com/post/day-17-new-time-zone-and-caves', 'https://www.mitspokes.com/post/day-16-memes-and-nicknames', 'https://www.mitspokes.com/post/day-15-bikin-and-bourbon', 
       'https://www.mitspokes.com/post/day-14-concerning-the-kentucky-leash-ban', 'https://www.mitspokes.com/post/day-13-spokes-goes-to-space-camp', 'https://www.mitspokes.com/post/day-12-who-let-the-dogs-and-other-animals-out', 'https://www.mitspokes.com/post/day-11-a-break-in-breaks', 'https://www.mitspokes.com/post/day-10-flat-tires-and-hilly-roads', 'https://www.mitspokes.com/post/day-9-you-gotta-do-it-everyday', 'https://www.mitspokes.com/post/on-the-road-again', 'https://www.mitspokes.com/post/day-7-planks-on-plank', 'https://www.mitspokes.com/post/day-6-virginia-is-for-lovers',
         'https://www.mitspokes.com/post/day-5-sweet-tea-baby', 'https://www.mitspokes.com/post/day-6', 'https://www.mitspokes.com/post/day-3-a-necessary-res-e-t-day', 'https://www.mitspokes.com/post/day-2-first-day-on-the-road-scenic-views-in-virginia-chaos-tacos-and-more-chaos', 'https://www.mitspokes.com/post/day-1-spokes-first-learning-festival']

def seperate_blogs(l):
    good_urls = []
    bad_urls = []
    for url in l:
        if "day" in url and get_blog_number(url):
            good_urls.append(url)
        else:
            bad_urls.append(url)
    return good_urls, bad_urls

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

def get_blog_number(url):
    blog_num = ""
    found_first_number = False
    for char in url:
        if char.isnumeric():
            blog_num += char
            found_first_number = True
        elif found_first_number:
            return int(blog_num)

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
        title = soup.find('span', {'class' : 'blog-post-title-font blog-post-title-color'})

        return blog
    return None

# print("calculating...")
# urls.sort(key=get_blog_number)
# print(scrape_blog("https://www.mitspokes.com/post/day-65-me-and-the-flies-against-the-world"))
#print(scrape_blog("https://www.mitspokes.com/post/day-72-the-promised-lands-portugal-and-sacramento"))
# good, bad = seperate_blogs(urls)
# print(bad)

sorted_urls = ['https://www.mitspokes.com/post/day-1-spokes-first-learning-festival', 'https://www.mitspokes.com/post/day-2-first-day-on-the-road-scenic-views-in-virginia-chaos-tacos-and-more-chaos', 'https://www.mitspokes.com/post/day-3-a-necessary-res-e-t-day','https://www.mitspokes.com/post/day-6', 'https://www.mitspokes.com/post/day-5-sweet-tea-baby', 'https://www.mitspokes.com/post/day-6-virginia-is-for-lovers', 
               'https://www.mitspokes.com/post/day-7-planks-on-plank', 'https://www.mitspokes.com/post/on-the-road-again', 'https://www.mitspokes.com/post/day-9-you-gotta-do-it-everyday', 'https://www.mitspokes.com/post/day-10-flat-tires-and-hilly-roads', 'https://www.mitspokes.com/post/day-11-a-break-in-breaks', 'https://www.mitspokes.com/post/day-12-who-let-the-dogs-and-other-animals-out', 'https://www.mitspokes.com/post/day-13-spokes-goes-to-space-camp', 
               'https://www.mitspokes.com/post/day-14-concerning-the-kentucky-leash-ban', 'https://www.mitspokes.com/post/day-15-bikin-and-bourbon', 'https://www.mitspokes.com/post/day-16-memes-and-nicknames', 'https://www.mitspokes.com/post/day-17-new-time-zone-and-caves', 'https://www.mitspokes.com/post/day-18-longest-day-of-the-year', 'https://www.mitspokes.com/post/day-19-bowling-green-learning-festival',
                'https://www.mitspokes.com/post/day-20-bushwhacking-and-gravel-riding', 'https://www.mitspokes.com/post/day-21-a-day-on-4-wheels', 'https://www.mitspokes.com/post/day-22-it-s-worth-it-the-sunsets', 'https://www.mitspokes.com/post/day-23', 'https://www.mitspokes.com/post/day-24-a-rest-day-in-saint-louis', 'https://www.mitspokes.com/post/day-25-no-more-cars', 'https://www.mitspokes.com/post/day-26-am-i-dreaming', 
                'https://www.mitspokes.com/post/day-27-41-million-revolutions', 'https://www.mitspokes.com/post/we-have-the-tour-de-france-at-home-jk', 'https://www.mitspokes.com/post/day-29-pick-your-poison', 'https://www.mitspokes.com/post/day-30-kansas-entrance-exam', 'https://www.mitspokes.com/post/day-31-castles-bubble-wands-and-everything-in-between', 'https://www.mitspokes.com/post/day-32-murica', 'https://www.mitspokes.com/post/day-33-viva-la-vida',
                'https://www.mitspokes.com/post/day-34-which-mit-spokes-member-are-you', 'https://www.mitspokes.com/post/day-35-i-don-t-think-we-re-in-kansas-anymore', 'https://www.mitspokes.com/post/day-36-when-we-re-big-kids', 'https://www.mitspokes.com/post/day-37-junk-in-our-trunk-what-i-packed-for-spokes', 'https://www.mitspokes.com/post/day-38-it-s-jolene-s-world-and-we-re-all-just-living-in-it', 
                'https://www.mitspokes.com/post/day-39-we-re-not-in-kansas-anymore-2', 'https://www.mitspokes.com/post/denver-rest-day', 'https://www.mitspokes.com/post/day-41-mother-infrastructure', 'https://www.mitspokes.com/post/day-42-reckoning-with-mortality', 'https://www.mitspokes.com/post/day-43-i-think-my-life-might-be-better-if-i-lived-in-colorado-mmm', 'https://www.mitspokes.com/post/day-44-spokes-vs-the-continental-divide', 
                'https://www.mitspokes.com/post/day-45-a-goated-day', 'https://www.mitspokes.com/post/day-46-call-us-james-cause-it-s-getting-peachy', 'https://www.mitspokes.com/post/what-i-eat-in-a-day', 'https://www.mitspokes.com/post/day-48-yay-utah', 'https://www.mitspokes.com/post/day-49-delicate-knees-at-delicate-arch', 'https://www.mitspokes.com/post/day-50-sunsets-and-moonrises', 'https://www.mitspokes.com/post/day-51-jackass-joe-s', 
                'https://www.mitspokes.com/post/day-52-ah-shit-here-we-go-again', 'https://www.mitspokes.com/post/day-53-we-can-t-read-signs', 'https://www.mitspokes.com/post/day-54-cosmic-gratitude', 'https://www.mitspokes.com/post/day-55-moo-and-hoodoo-and-food', 'https://www.mitspokes.com/post/look-on-the-bryce-side', 'https://www.mitspokes.com/post/day-57-diary-of-a-limpy-kid', 'https://www.mitspokes.com/post/day-58-angels-landing-and-angel-s-departing',
                'https://www.mitspokes.com/post/day-59-spokes-in-the-narrows', 'https://www.mitspokes.com/post/day-60-a-how-to-guide-for-boring-rides', 'https://www.mitspokes.com/post/day-61-desert-magic', 'https://www.mitspokes.com/post/day-62-senioritis', 'https://www.mitspokes.com/post/day-63-we-love-stickers', 'https://www.mitspokes.com/post/day-64-a-non-biking-day-in-portugal', 
                'https://www.mitspokes.com/post/day-65-me-and-the-flies-against-the-world', 'https://www.mitspokes.com/post/day-66-the-oasis-of-nevada', 'https://www.mitspokes.com/post/day-67-one-final-ass-whooping-from-nevada', 'https://www.mitspokes.com/post/day-69-lifestyle-whiplash', 'https://www.mitspokes.com/post/day-69-the-first-of-many-lasts', 'https://www.mitspokes.com/post/day-70-the-curse-ends', 
                'https://www.mitspokes.com/post/day-71-bumming-around-savoring-every-moment', 'https://www.mitspokes.com/post/day-72-the-promised-lands-portugal-and-sacramento', 'https://www.mitspokes.com/post/day-73-28-things-you-have-to-do-before-we-both-die', 'https://www.mitspokes.com/post/day-74-the-finale', 'https://www.mitspokes.com/post/day-75-the-real-spokes-ogs']

def get_sorted_blog_urls():
    """
    returns the blog URLs in order starting with day 1
    """
    return sorted_urls