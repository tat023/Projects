from bs4 import BeautifulSoup
import requests
import os


class URL:
    """Represents the URLs relevant to the inputted keywords. The parameters are a link from a website, named link. """

    def __init__(self, link):
        self._link = link
        self._keywords = []

    def scrape(self, keywords):
        """Returns the results from the URL object using BeautifulSoup and Requests to scrape. The parameter keywords
        is a list of strings and this allows to user to scrape for specific words and phrases."""
        self._keywords = keywords
        relevant_links = []
        test_page = requests.get(self._link)
        soup = BeautifulSoup(test_page.text, "html.parser")
        link_names = soup.find_all('a')
        if test_page.status_code == 200:
            for link in link_names:
                link_text = link.get_text()
                for word in self._keywords:
                    if word.lower() in link_text.lower():
                        url = str(link.get('href'))
                        relevant_links.append(url)
        return relevant_links


class TextFile:
    """Represents a textfile object with methods to create, add, remove, edit a textfile with the data from the URL
    object"""

    def __init__(self):
        self._urls = ''
        self._text_file = ''
    def get_file(self):
        """Method that returns self._text_file"""
        return self._text_file

    def create_file(self, urls):
        """Function creates a text file with the links of the search results and saves the file into a read only
        format"""
        self._urls = urls
        with open('links.txt', 'w') as self._text_file:
            for elements in self._urls:
                url_string = str(elements)
                self._text_file.write(url_string + '\n')
       # os.chmod(self._text_file, 0o444)
    #def edit_file(self, text_file):
        """Function makes the text file writeable and edits the read only file from the function create_file.
        The parameter text_file is the TextFile object created"""
     #   self._text_file = text_file
      #  os.chmod(self._text_file, 0o644)







def main():
    url_name = "https://legal.yahoo.com/us/en/yahoo/privacy/index.html"
    key_words = ['privacy']
    url_object = URL(url_name)
    url = url_object.scrape(key_words)
    print(url)
    file = TextFile()
    file.create_file(url)
    print(file.get_file())


if __name__ == '__main__':
    main()
