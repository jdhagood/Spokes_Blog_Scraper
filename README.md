# Spokes_Blog_Scraper

This is a project to scrape all the blogs on the [Spokes 2024 website](https://www.mitspokes.com/blog) and convert it into a yearbook. 

We use selenium to scrape all the blog URLs off the (https://www.mitspokes.com/blog) page because it is dynamically loaded. After that we use BS4 with requests to scrape each blog. For each blog we keep track of the author, title, paragraphs, and images. 

TODO: Take all the scraped data and autoformat it into a yearbook
