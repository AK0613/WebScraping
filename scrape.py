import requests
from bs4 import BeautifulSoup
import pprint


# . for classes # for ids

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        # title = links[index].getText() this is equivalent because we are enumerating over links
        title = item.getText()
        href = item.find('a').get('href')
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


urls = ('https://news.ycombinator.com/news', 'https://news.ycombinator.com/news?p=2')

for item in urls:
    res = requests.get(item)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    custom_hn = sorted(create_custom_hn(links, subtext), key=lambda d: d['votes'], reverse=True)
    with open('Links.txt', 'a') as output_file:
        pprint.pprint(custom_hn, output_file, sort_dicts=False)
