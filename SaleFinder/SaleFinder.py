from bs4 import BeautifulSoup
import requests


class URL:
    """Represents the URLs relevant to the inputted keywords. The parameters are a link from a website and a list of
    words. """

    def __init__(self, link):
        self._link = link

    def scrape(self, keywords):
        """Returns the results from the URL object using BeautifulSoup and Requests to scrape. The parameter keywords
        allows to user to scrape for specific phrases."""
        self._keywords = keywords
        test_page = requests.get(self._link)
        soup = BeautifulSoup(test_page.text, "html.parser")
        link_names = soup.find_all('a')
        if test_page.status_code == 200:
            for link in link_names:
                link_text = link.get_text()
                for word in self._keywords:
                    if word.lower() in link_text.lower():
                        url = link.get('href')
                        print(url)


class TextFile:
    """Represents a textfile object with methods to add, remove, edit a textfile with the data from the URL object"""


def main():
    url_name = "https://news.search.yahoo.com/search;_ylt=AwrO6mi2JcRkrHcLDjPQtDMD;_ylu" \
               "=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=shopping+clearance+sale&pz=10&fr=uh3_news_web&fr2=sb" \
               "-top&bct=0&b=1&pz=10&bct=0&xargs=0"
    key_words = ['close', 'closure', 'closing', 'nordstrom', 'target']
    url_objet = URL(url_name)
    url_objet.scrape(key_words)


if __name__ == '__main__':
    main()
