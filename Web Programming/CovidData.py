"""
This is to show simple COVID-19 into fetching from worldodometers site using lxml
* The main motivation to use lxml in place of bs4 is that is faster and therefore
more convenient to use in Python web projecys
"""

from typing import NamedTuple
import requests
from lxml import html


class CovidData(NamedTuple):
    cases: int
    deaths: int
    recovered: int


def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> CovidData:
    xpath_str = "//div[@class='maincounter-number']/span/text()"
    return CovidData(
        *html.fromstring(requests.get(url, timeout=10).content).xpath(xpath_str)
    )


fmt = """Total COVID-19 cases in the world: {}
Total COVID-19 deaths in the world: {}
Total COVID-19 recovered in the world: {}"""
print(fmt.format(*covid_stats()))
