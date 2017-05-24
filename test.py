import urllib.request
from bs4 import BeautifulSoup
from google import search

lst = []
all_links = ['http://www.gemschicago.org Tuition',
        'https://www.latinschool.org Tuition',
        'http://www.nordangliaeducation.com Tuition',
        'http://www.fwparker.org Tuition']
for link in all_links:
    for url in search(link,lang='en',stop=3):
        lst.append(url)
    search_link = lst[0]
    request = urllib.request.Request(search_link)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    print('---------------------------------------------------------------')
    print(search_link)
    for table_tag in soup.find_all('td'):
        print(table_tag.text)
    lst = []
