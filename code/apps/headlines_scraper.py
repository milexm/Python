import requests
from bs4 import BeautifulSoup

class HeadlineScraper:
    def __init__(self, url):
        """
        Initialize the scraper with the specified URL.
        
        Parameters:
        - url (str): The URL of the web page to scrape.
        """
        self.url = url
        
    def scrape(self):
        """
        Retrieve the HTML content of the specified URL and parse it
        using BeautifulSoup to extract a list of headlines.
        
        Returns:
        - headlines (list): A list of strings, where each string is a headline.
        """
        # Fetch the HTML content of the webpage
        response = requests.get(self.url)
        html = response.text
        
        # Parse the HTML content
        soup = BeautifulSoup(html, "html.parser")
        
        # Find all the elements with the "h2" tag
        headline_elements = soup.find_all("h2")

        # Extract the text content of each element and store it in a list
        headlines = [elem.text for elem in headline_elements]
        
        return headlines

# Create a scraper for a specific URL
# url = "https://realpython.github.io/fake-jobs/"

""" 
url = 'https://www.geeksforgeeks.org/python-programming-language/'

scraper = HeadlineScraper(url)

# Scrape the headlines
headlines = scraper.scrape()
print(headlines)

"""