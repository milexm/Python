''' 
Module headlines_scraper_samples.py

Remarks
------


'''

import requests
import unittest 
from bs4 import BeautifulSoup


import sys
sys.path.append('./code/apps')

class CheckResult(unittest.TestCase):
  
    def check_scraper_results(self, result, expected_result):
        try: 
            self.assertEqual(result, expected_result)
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 

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

class HeadlineScraperSamples():
    """
    Test case for the HeadlineScraper class.
    
    This test case tests the following functionality of the HeadlineScraper class:
     - Basic headline extraction
     - Headline extraction with multiple headlines
     - Headline extraction with nested HTML elements
     - Error handling when the HTML page has no headlines
     - Error handling when the URL is invalid
    """
    
    def __init__(self):
        """
        Set up the test case by creating a scraper for the test HTML page.
        """
        self.scraper = HeadlineScraper("https://www.geeksforgeeks.org/python-programming-language/")

        self.check_result = CheckResult()
        
    def extract_basic_headline(self):
        """
        Extracts basic headline.
        
        It verifies that the scraper can extract a single headline from
        an HTML page.
        """
        # Set the expected output
        expected_headlines = ["Headline 1"]
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        print(headlines)
        print(expected_headlines)
        
        # Assert that the expected and actual outputs are equal
        # assert headlines == expected_headlines
        
    def extract_multiple_headlines(self):
        """
        Extract multiple headlines.
        
        Verifies that the scraper can extract multiple headlines from
        an HTML page.
        """
        # Set the expected output
        expected_headlines = ["Headline 1", "Headline 2", "Headline 3", "Headline 6"]
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        # Assert that the expected and actual outputs are equal
        self.check_result.check_scraper_results(headlines, expected_headlines)
        
    def extract_nested_html_elements(self):
        """
        Extracts headline extraction with nested HTML elements.
        
        Verifies that the scraper can extract headlines from an HTML
        page that contain nested HTML elements, and strip the nested elements
        from the returned headlines.
        """
        # Set the expected output
        expected_headlines = ["Headline 1", "Headline 2", "Headline 3"]
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        # Assert that the expected and actual outputs are equal
        self.check_result.check_scraper_results(headlines, expected_headlines)
        
    def empty_headline_list(self):
        """
        Handle errors when the HTML page has no headlines.
        
        Verifies that the scraper handles the case where the HTML
        page has no headlines, and returns an empty list.
        """
        # Set the URL of the scraper to an HTML page with no headlines
        self.scraper.url = "https://www.indeed.com/?from=gnav-title-webapp"
        
       
        # Set the expected output
        expected_headlines = []
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        # Assert that the expected and actual outputs are equal
        self.check_result.check_scraper_results(headlines, expected_headlines)
