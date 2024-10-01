import re
import os
import requests
from bs4 import BeautifulSoup
from blog_urls import get_sorted_blog_urls

# Function to clean up titles for use in file/folder names
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def get_soup(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def get_images(url, dir):
    def clean_image_urls(urls):
        cleaned_urls = []
        for url in urls:
            if "/v1" in url:
                cleaned_url = url[:url.index("/v1")]
            else:
                cleaned_url = url  # Keep the original URL if "/v1" is not found
            if cleaned_url not in cleaned_urls:
                cleaned_urls.append(cleaned_url)
        return cleaned_urls

    # Create directory if it doesn't exist
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Send a GET request to the webpage
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return
    
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags and extract their src attributes
    images = soup.find_all('img')
    image_sources = clean_image_urls([img['src'] for img in images if 'src' in img.attrs])

    # Download and save each image
    for idx, img_url in enumerate(image_sources):
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(dir, f"image_{idx + 1}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")

# Function to scrape blog content (title, author, etc.)
def scrape_blog(url):
    soup = get_soup(url)
    if soup is None:
        return f"Failed to get soup for {url}"

    blog = {
        "url": url,
        "title": None,
        "by": None,
        "ride info": None,
        "body": None,
        "image dir": None
    }

    try:
        title_elem = soup.find('span', class_="blog-post-title-font blog-post-title-color")
        title = title_elem.get_text(strip=True) if title_elem else "No Title Found"
        blog["title"] = title

        by_elem = soup.find('span', class_="tQ0Q1A user-name dlINDG")
        blog['by'] = by_elem.get_text(strip=True) if by_elem else "No Author Found"

        # Sanitize the blog title for use as a folder name
        sanitized_title = sanitize_filename(title)
        blog_image_dir = os.path.join("images", sanitized_title.replace(' ', '_'))

        # Download images to the sanitized folder
        get_images(url, blog_image_dir)
        blog["image dir"] = blog_image_dir

    except Exception as e:
        print(f"Error scraping blog {url}: {e}")

    return blog

# Main function
def main():
    # Example usage:
    blog_urls = get_sorted_blog_urls()
    for url in blog_urls:
        blog_data = scrape_blog(url)
        print(blog_data)

if __name__ == "__main__":
    main()
