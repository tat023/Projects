from bs4 import BeautifulSoup
import requests
url_name = "https://news.search.yahoo.com/search;_ylt=AwrO6mi2JcRkrHcLDjPQtDMD;_ylu" \
           "=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=shopping+clearance+sale&pz=10&fr=uh3_news_web&fr2=sb" \
           "-top&bct=0&b=1&pz=10&bct=0&xargs=0"
test_page = requests.get(url_name)
soup = BeautifulSoup(test_page.text, "html.parser")
key_word = ['close', 'closure', 'closing', 'nordstrom', 'target']
link_names = soup.find_all('a')
if test_page.status_code == 200:
    for link in link_names:
        link_text = link.get_text()
        for word in key_word:
            if word.lower() in link_text.lower():
                url = link.get('href')
                print(url)
