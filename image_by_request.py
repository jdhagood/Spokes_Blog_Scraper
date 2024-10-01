import requests
from bs4 import BeautifulSoup
import os

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

# Example usage
get_images('https://www.mitspokes.com/post/day-14-concerning-the-kentucky-leash-ban', "images/ky")
