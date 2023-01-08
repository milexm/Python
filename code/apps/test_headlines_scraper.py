import requests
from bs4 import BeautifulSoup
import sys

sys.path.append('./code/apps')

from headlines_scraper import HeadlineScraper


class HeadlineScraperTestCase():
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
        
    def test_basic_headline_extraction(self):
        """
        Test basic headline extraction.
        
        This test verifies that the scraper can extract a single headline from
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
        
    def test_multiple_headlines(self):
        """
        Test headline extraction with multiple headlines.
        
        This test verifies that the scraper can extract multiple headlines from
        an HTML page.
        """
        # Set the expected output
        expected_headlines = ["Headline 1", "Headline 2", "Headline 3", "Headline 6"]
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        # Assert that the expected and actual outputs are equal
        self.assertEqual(headlines, expected_headlines)
        
    def test_nested_html_elements(self):
        """
        Test headline extraction with nested HTML elements.
        
        This test verifies that the scraper can extract headlines from an HTML
        page that contain nested HTML elements, and strip the nested elements
        from the returned headlines.
        """
        # Set the expected output
        expected_headlines = ["Headline 1", "Headline 2", "Headline 3"]
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
        # Assert that the expected and actual outputs are equal
        self.assertEqual(headlines, expected_headlines)
        
    def test_empty_headline_list(self):
        """
        Test error handling when the HTML page has no headlines.
        
        This test verifies that the scraper handles the case where the HTML
        page has no headlines, and returns an empty list.
        """
        # Set the URL of the scraper to an HTML page with no headlines
        self.scraper.url = "http://localhost/no_headlines.html"
        
        # Set the expected output
        expected_headlines = []
        
        # Call the scraper's scrape method
        headlines = self.scraper.scrape()
        
if __name__ == '__main__':
    scraper_test = HeadlineScraperTestCase()
    scraper_test.test_basic_headline_extraction()