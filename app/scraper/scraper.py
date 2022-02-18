from urllib.request import urlopen
from bs4 import BeautifulSoup

import scraper_utils.utils as utils
URL_BASE = 'https://coronavirus.es.gov.br/painel-covid-19-es'

class CovidScraper:
    """
    Scraper responsible of obtaining csv files of covid related cases in
    the state of Espirito Santo in Brazil.
    """

    def __init__(self, url:str=URL_BASE) -> None:
        self.__url = url

    def generate_csv_file_url(self):
        html = utils.get_html_doc(self.__url)
        soup = BeautifulSoup(html, "html.parser")

        download_panel = soup.find_all("div", {"class": "span-12 col-xs-12 col-md-12 col-sm-12 col-lg-12"})
        link_soups = BeautifulSoup(str(download_panel), "html.parser")
        panel_links = link_soups.find_all("a")
        data = panel_links[0]

        return data.get("href")

def test():
    scraper = CovidScraper()
    download_link = scraper.generate_csv_file_url()
    utils.download_csv(download_link, 'files/microdados.csv')

if __name__ == "__main__":
    test()