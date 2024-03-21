from requests_html import HTMLSession
from sql_insert import insertDatabase
import requests as req

def main():
    
    url = "https://letterboxd.com/abdullahaktan/list/oscar-winners/"

    session = HTMLSession()

    with session.get(url) as site:

        divs = site.html.find("div")

        links = []

        for item in divs:
            if 'data-target-link' in item.attrs:
                links.append(item.attrs['data-target-link'])


    films = {}

    for item in links:

        url = "https://letterboxd.com/csi" + item + "rating-histogram/"

        with session.get(url) as site:

            classes = site.html.find("a")

            title = item.replace("-", " ").replace("/film/", "").replace("/", "").capitalize()

            ratings = []

            for item in classes:
                if "ratings" in str(item.text):
                    value = int(str(item.text).replace(",", "").split()[0])
                    ratings.append(value)

        films[title] = ratings

    insertDatabase(films)

if __name__ == "__main__":
    main()
