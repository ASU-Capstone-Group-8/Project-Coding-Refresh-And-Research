## Task-21 Data Collection and Preparation for NLP Models Research 
Date: 01 October 2024

# Data Acquisition:

Gathering raw text data in preparation for text cleaning and then preprocessing.

### Potential methods:
 - Manual import into the project: 
   - This can be done for situations where the text is already in a plain text format (situations where we do not need to pull it from a specified source like a news article or social media post).
 - Web Scraping: 
   - Use of tools to pull the text directly from a webpage.
   - Potential avenues:
     - Build our own web-scraper:
       - Advantages:
         - Can tailor it to our needs
         - Can use APIs for sites that we will pull from if they exist
         - Gives us freedom for how the pulled data is formatted
       - Disadvantages:
         - May be more trouble than it is worth
           - We have to consider factors like frequency of API calls or making resource requests from websites, since this could turn into an unintentional psuedo-DDoS problem if we don't work the appropriate preventative measures in place (limit # of requests per period of time).
           - There are already existing tools and libraries that do this already, and some appear to be low cost or free.
         - APIs will inevitably cost money, and the price will increase depending on the magnitude of calls made.
         - 
     - Using a tool like BeautifulSoup (https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)):
       - Parses HTML/XML documents, and generates a parse tree
       - It is not a web-scraper by itself, but it gives virtually all of the necessary functionality for getting us most of the way there.
       - Advantages:
         - It is implemented using python, making it ideal for us since we will be coding in python.
         - Easy to configure and get working
       - Disadvantages:
         - Lots of dependencies
         - Not as scalable (based on articles)
     - Using Scrapy (https://scrapy.org/):
       - An open source project used for extracting data from web pages.
       - This tool is a webscraper, and is ready to go right out of the box
       - Advantages:
         - Designed specifically for web scraping.
         - Great for larger-scale projects.
       - Disadvantages:
         - Can be difficult to learn how to use.
     - Using a combination of Scrapy and BeautifulSoup:
       - This may be another option, especially since they can be configured together.
       - A good breakdown can be found at https://oxylabs.io/blog/scrapy-vs-beautifulsoup.

# Text Cleaning:


## General Overview:
 - Article reviewed for research (https://www.analyticsvidhya.com/blog/2022/01/text-cleaning-methods-in-nlp/)
   - Outlines all of the general steps of cleaning data that will be used for NLP model training
 - Process of removing unwanted artifacts from raw text, prior to preprocessing the raw data.
 - Types: 
   - Unicode Normalization: Removal or conversion of symbols, graphic chars or special chars. 
   - Regex: Used for searching and/or filtering text from data. 
   - Spelling corrections: Can use a corpus of most mis-typed words to replace spelling errors.
   - Case Normalization: Converting all words to a lowercase (uniform) state.
 - This is actually pretty simple, and many of the tools we will be testing out perform this step by default during preprocessing (PyTorch and TensorFlow).
