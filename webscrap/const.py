from re import compile, escape

GET_TARGET = 'https://myanimelist.net'
GET_QUERY_BASE = '?type=&limit='  # without defined values redirects to DEFAULT_REDIRECT
GET_QUERY_OPT = ['tv', 'movie', 'ova', 'ona', 'special', 'type', 'limit']  # limit default is 0; limit range default is 50
GET_DEFAULT_REDIRECT = 'https://myanimelist.net/topanime.php'  # default redirect when queries 'type' and/or 'limit' are not properly defined
GET_URL_LIST = [
    'https://myanimelist.net/topanime.php?type=tv',
    'https://myanimelist.net/topanime.php?type=movie',
    'https://myanimelist.net/topanime.php?type=ova',
    'https://myanimelist.net/topanime.php?type=ona',
    'https://myanimelist.net/topanime.php?type=special'
]

URL_BASE = 'https://myanimelist.net'
URL_ANIME_BASE = 'https://myanimelist.net/anime/'  # ../anime/anime_id_query/[optional_anime_name_is_not_necessary_to_getreq]
URL_ANIME_PATH = '/anime/'

# Regex patterns
PATTERNS = {
    "base_url": compile(rf"{escape(URL_BASE)}/?$"),
    "anime_url": compile(rf"{escape(URL_ANIME_BASE)}/\d+/.+?"),
    "default_redirect": compile(rf"{escape(GET_DEFAULT_REDIRECT)}{escape('?')}?(type|limit=\d+)?")
}

# Output-related constants
OUTPUT_FILE_NAME = 'urls_list.csv'
OUTPUT_PATH = ''
CSV_HEAD = ['anime_url', 'broadcast', 'anime_id_query']