from datetime import datetime
from re import compile, match
from main import beauty



first_year = '1917'
current_year = f"{datetime.now().year}"
anime_url_const = 'https://myanimelist.net/anime/'
anime_url_const_pattern = compile(r"^https://myanimelist.net/anime/\d+/.+$")
base_url = 'https://myanimelist.net/anime/season/'

seasons = ('fall', 'summer', 'spring', 'winter')
anime_tuple_struct = ['id', 'name', 'year', 'season', 'url']  # csv headers
html_filters = {'anchor': {
    'class': 'link-title',
    'url': 'href',
    'txt': 'innerText'
}}



def select_html_filter(filter_name: str, values: list, filter_list: dict = html_filters):
    key_list = filter_list.get(filter_name)
    if key_list is None:
        return []

    return [key_list for k in values if values[k]]

def select_season(season: str, season_list: list | tuple = seasons):
    return season_list.remove(season)

def get(domain, url):
    import http.client as c

    class PageNotFound(Exception): pass

    conn = c.HTTPSConnection(domain)
    conn.request('GET', url)
    resp = conn.getresponse()

    if resp.status != 200:
        conn.close()
        raise PageNotFound(f'Error to fetch the url {url}')
    if resp.url == base_url:
        conn.close()
        raise Exception(f'Error to fetch the url {url}; it is a default redirect from the server')

    data = resp.read().decode()

    conn.close()
    return data

def parse_anchors(resp):
    anchor_filter = html_filters.get('anchor')
    if not anchor_filter:
        raise ValueError("Anchor filter is not defined in html_filters")

    anchor_href = anchor_filter.get('url')
    class_title = anchor_filter.get('class')

    if not anchor_href or not class_title:
        raise ValueError("Anchor filter is missing required keys: 'url' or 'class'")

    anchors = beauty(resp).find_all('a', class_=class_title)
    return [anchor.get(anchor_href) for anchor in anchors if anchor.get(anchor_href)]

def extract_anchor_data(anchor_list: list):
    l = beauty([anchor_list for a in anchor_list if match(anime_url_const_pattern, a)])