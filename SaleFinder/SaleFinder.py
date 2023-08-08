from bs4 import BeautifulSoup
import requests


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

    def create_file(self, urls):
        self._urls = urls
        with open('links.txt', 'w') as self._file:
            for elements in self._urls:
                url_string = str(elements)
                self._file.write(url_string + '\n')


def main():
    url_name = "https://news.search.yahoo.com/search;_ylt=AwrO6mi2JcRkrHcLDjPQtDMD;_ylu" \
               "=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=shopping+clearance+sale&pz=10&fr=uh3_news_web&fr2" \
               "=sb-top&bct=0&b=1&pz=10&bct=0&xargs=0"
    key_words = ['close', 'closure', 'closing', 'nordstrom', 'target']
    url_object = URL(url_name)
    url = url_object.scrape(key_words)
    print(url)  # this is a list
    file = TextFile()
    file.create_file(url)


if __name__ == '__main__':
    main()
