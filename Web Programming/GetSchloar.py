"""
Get the citation from Google Scholar
using title and year of publication, and volume and pages of journal.
"""

import requests
from bs4 import BeautifulSoup


def get_citation(base_url: str, params: dict) -> str:
    """
    Return the citation number.
    """
    try:
        soup = BeautifulSoup(
            requests.get(base_url, params=params, timeout=10).content, "html.parser"
        )
        div = soup.find("div", attrs={"class": "gs_ri"})
        if div:
            anchors = div.find("div", attrs={"class": "gs_fl"}).find_all("a")
            return anchors[2].get_text()
        else:
            return "Citation information not found."
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    params1 = {
        "title": (
            "Precisely geometry controlled microsupercapacitors for ultrahigh areal "
            "capacitance, volumetric capacitance, and energy density"
        ),
        "journal": "Chem. Mater.",
        "volume": 30,
        "pages": "3979-3990",
        "year": 2018,
        "hl": "en",
    }
    print(get_citation("https://scholar.google.com/scholar_lookup", params=params1))

    params2 = {
        "title": (
            "Precisely geometry controlled microsupercapacitors for ultrahigh areal "
            "capacitance, volumetric capacitance, and energy density"
        ),
        "journal": "Chem. Mater.",
        "volume": 30,
        "pages": "3979-3990",
        "year": 2018,
        "hl": "en",
    }
    print(get_citation("https://scholar.google.com/scholar_lookup", params=params2))
