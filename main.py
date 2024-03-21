import requests as req
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

def main():
    
    url = "https://letterboxd.com/abdullahaktan/list/oscar-winners/"

    session = HTMLSession()

    with session.get(url) as site:

        divs = site.html.find("div")

        links = []

        for item in divs:
            if 'data-target-link' in item.attrs:
                links.append(item.attrs['data-target-link'])

    for item in links:

        url = "https://letterboxd.com/csi" + item + "rating-histogram/"

        with session.get(url) as site:

            print(site.text)

            #titles = site.html.find("title")

            #for item in titles:
            #    print(item.text)

if __name__ == "__main__":
    main()
