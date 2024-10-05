## Practice and Sandboxing of Beautiful Soup For Web Scraping

### Components Used:
 - BeautifulSoup Library:
   - This helps to get the raw html data into a usable data structure for ease of extracting html elements
   - i.e., it helps pull things like author, title, body of a cnn article by id/class names
 - Requests Library:
   - This pulls the actual web page from its location based on the url
   - Works well with BeautifulSoup

### Potential Application:
We may be able to use base class, that we can extend to additional implementation classes (children), such that we have 
scrapers for various websites. This could be done by trying to map out the general html structure of the target websites
and then using the discovered class/id names for the data we are targeting, and then use these to define the specific sub-classes
(i.e., a class that can process articles from CNN, FoxNews, Twitter, etc.). 

This would work relatively well with Argilla, which would take the scraped data, and provide the means of labeling the data.
All that would be necessary, would be to build a web application that can scrape the data into a convenient location, and 
then set up argilla to pull the scraped data and make it available for annotation. 