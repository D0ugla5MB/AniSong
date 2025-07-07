# the 'GET_' refers to http get request the respective func does
from typing import NewType

HTML = NewType('HTML', str)

def get_urls(args: str):
    """
        args might be from GET_URL_LIST or some referenced url of the previous mentioned value using ['tv','movie','ova','ona','special']
    """
    
    pass

def check_args(args: str)-> bool: # from get_urls' args
    pass

def check_chunks(data: HTTPResponse) -> HTML: # type: ignore
    """
        fetch a specific range from the returned html file
    """
    pass

def treat_resp(resp: HTML) -> bool: # from HTTP GET METHOD returned by get_urls
    pass

def build_csv(src: __file__):
    pass

GET_TARGET='https://myanimelist.net'
GET_QUERY_BASE = '?type=&limit=' # without defined values redirects to DEFAULT_REDIRECT 
GET_QUERY_OPT = ['tv','movie','ova','ona','special', 'type','limit'] # limit default is 0; limit range default is 50
GET_DEFAULT_REDIRECT = 'https://myanimelist.net/topanime.php' # default redirect when queries 'type' and/or 'limit' are not properly defined
GET_URL_LIST = [
    'https://myanimelist.net/topanime.php?type=tv',
    'https://myanimelist.net/topanime.php?type=movie',
    'https://myanimelist.net/topanime.php?type=ova',
    'https://myanimelist.net/topanime.php?type=ona',
    'https://myanimelist.net/topanime.php?type=special'
]

URL_BASE='https://myanimelist.net'
URL_ANIME_BASE='https://myanimelist.net/anime/' #../anime/anime_id_query/[optional_anime_name_is_not_necessary_to_getreq]
OUTPUT_FILE_NAME = 'urls_list.csv'
OUTPUT_PATH = ''
CSV_HEAD = ['anime_url','broadcast','anime_id_query']