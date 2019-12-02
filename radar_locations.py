from requests import get, Response
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from typing import Union
import pandas as pd

from urllib3.response import HTTPResponse


def _simple_get(url: str) -> Union[HTTPResponse, None]:
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.

    :param url: URL of website to GET.
    :return: HTTPResponse class or None.
    """

    try:
        with closing(get(url, stream=True)) as resp:
            if _is_good_response(resp):
                return resp.content
            return None

    except RequestException as e:
        return None


def _is_good_response(resp: Response) -> bool:
    """
    Returns True if the response seems to be HTML, False otherwise.

    :param resp: Response class from requests get call.
    :return: True or false boolean.
    """

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def _parse_html(url: str) -> BeautifulSoup:
    """
    Gets HTML data from website being scraped.

    :param url: URL of website to scrape.
    :return: BeautifulSoup object.
    """

    raw_html = _simple_get(url)

    if raw_html:
        return BeautifulSoup(raw_html, 'html.parser')
    raise IOError("Couldn't GET any HTML data using the provided url.")


def scrape_radar_info(url: str) -> pd.DataFrame:
    """
    Retrieve table of radar lat/lon info.

    :param url: URL of website to scrape.
    :return: Dataframe with radar lat/lon info.
    """
    soup = _parse_html(url)
    table = soup.find('table').prettify()
    return pd.read_html(table)[0]


# scrape table of radar location info
df = scrape_radar_info("http://apollo.lsc.vsc.edu/classes/remote/lecture_notes/radar/88d/88D_locations.html")
# need columns 1 and 3

# create new data frame with station id's and lat/lon locations
df2 = df[[1, 3]]

# split lat/lon column into individual columns
new = df2[3].str.split("/", n=1, expand=True)
df2["Lat"] = new[0]
df2["Lon"] = new[1]
df2.drop(columns=3, inplace=True)
df2.drop(df2.index[0],inplace=True)
df2.rename(columns={1: "Id"}, inplace=True)

# add decimals and convert lat/lons to floats
for i, j in enumerate(zip(df2["Lat"], df2["Lon"])):
    df2.at[i+1, "Lat"] = float((j[0][:2] + '.' + j[0][2:]).strip('E'))
    df2.at[i+1, "Lon"] = float((j[1][:4] + '.' + j[1][4:]).strip('E')) * -1


# export radar lat/lon locations
df2.to_csv("radar_lat_lon.csv", index=False)
